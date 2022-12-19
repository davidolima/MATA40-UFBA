from cFila import Fila
from cPaciente import Paciente
from cLeito import Leito
from cPilha import Pilha
from funcAux import faixaEtaria

import random

class Simulador:
    def __init__(self):
        self.logs = Fila()

        # Neonatal
        self.__total_nn__ = 0
        self.__tt_leitos_nn__ = 0
        self.__leitos_nn__ = Pilha()
        self.__nn_p_urg__ = Fila()
        self.__nn_m_urg__ = Fila()
        self.__nn_emerg__ = Fila()
        # Pediatrica
        self.__total_pd__ = 0
        self.__tt_leitos_pd__ = 0
        self.__leitos_pd__ = Pilha()
        self.__pd_p_urg__ = Fila()
        self.__pd_m_urg__ = Fila()
        self.__pd_emerg__ = Fila()
        # Adulto
        self.__total_ad__ = 0
        self.__tt_leitos_ad__ = 0
        self.__leitos_ad__ = Pilha()
        self.__ad_p_urg__ = Fila()
        self.__ad_m_urg__ = Fila()
        self.__ad_emerg__ = Fila()

        self.__fila_geral__ = Fila()

    def __str__(self):
        """
        Retorna o estado de cada fila disponível.
        """
        cor_normal = "\033[00m"
        cor_categoria = "\033[38;5;11m"
        cor_baixa_prioridade = "\033[38;5;226m"
        cor_media_prioridade = "\033[38;5;208m"
        cor_alta_prioridade = "\033[38;5;196m"

        out  = "\n" + "%s||||| CONTROLE DE LEITOS |||||%s"%(cor_categoria, cor_normal)

        out += "\n" + "%s[Neonatal]%s"%(cor_categoria, cor_normal)
        out += "\n" + "Total de pacientes:"+ ' ' + str(self.__total_nn__)
        out += "\n" + f"Leitos abertos ({self.__tt_leitos_nn__}): " + str(self.__leitos_nn__)
        out += "\n" + "%sUrgente%s:"%(cor_baixa_prioridade, cor_normal)
        out += "\n" + str(self.__nn_p_urg__)
        out += "\n" + "%sMuito Urgente%s:"%(cor_media_prioridade, cor_normal)
        out += "\n" + str(self.__nn_m_urg__)
        out += "\n" + "%sEmergência%s:"%(cor_alta_prioridade, cor_normal)
        out += "\n" + str(self.__nn_emerg__)

        out += "\n" + "\n%s[Pediátrico]%s"%(cor_categoria, cor_normal)
        out += "\n" + "Total de pacientes:"+ ' ' + str(self.__total_pd__)
        out += "\n" + f"Leitos abertos ({self.__tt_leitos_pd__}): " + str(self.__leitos_pd__)
        out += "\n" + "%sUrgente%s:"%(cor_baixa_prioridade, cor_normal)
        out += "\n" + str(self.__pd_p_urg__)
        out += "\n" + "%sMuito Urgente%s:"%(cor_media_prioridade, cor_normal)
        out += "\n" + str(self.__pd_m_urg__)
        out += "\n" + "%sEmergência%s:"%(cor_alta_prioridade, cor_normal)
        out += "\n" + str(self.__pd_emerg__)

        out += "\n" + "\n%s[Adulto]%s"%(cor_categoria, cor_normal)
        out += "\n" + "Total de pacientes:"+ ' ' + str(self.__total_ad__)
        out += "\n" + f"Leitos abertos ({self.__tt_leitos_ad__}): " + str(self.__leitos_ad__)
        out += "\n" + "%sUrgente%s:"%(cor_baixa_prioridade, cor_normal)
        out += "\n" + str(self.__ad_p_urg__)
        out += "\n" + "%sMuito Urgente%s:"%(cor_media_prioridade, cor_normal)
        out += "\n" + str(self.__ad_m_urg__)
        out += "\n" + "%sEmergência%s:"%(cor_alta_prioridade, cor_normal)
        out += "\n" + str(self.__ad_emerg__)

        out += "\n" + "%s\n[Log de Eventos]%s"%(cor_categoria, cor_normal)
        contador = 0
        while not self.logs.vazia():
            contador += 1
            out += '\n' + f"[{contador}]"+ ' ' + self.logs.remover()

        return out

    def novoLeito(self, f_etaria):
        """Adiciona um leito na contagem de leitos disponiveis."""

        novo_leito = Leito(f_etaria)

        self.logs.inserir(f"O hospital '{novo_leito.hospital}' acaba de disponibilizar o leito({novo_leito}) para a faixa etária '{f_etaria}'")
        if f_etaria == 'n':
            self.__leitos_nn__.empilhar(novo_leito)
            self.__tt_leitos_nn__ += 1
        elif f_etaria == 'p':
            self.__leitos_pd__.empilhar(novo_leito)
            self.__tt_leitos_pd__ += 1
        elif f_etaria == 'a':
            self.__leitos_ad__.empilhar(novo_leito)
            self.__tt_leitos_ad__ += 1

    def novoPaciente(self, paciente: Paciente, anuncio=True):
        """Adicionar paciente em sua devida fila."""

        if paciente.gravidade < 3 and anuncio:
            self.logs.inserir(f"Um novo paciente({paciente}) de idade {paciente.idade} em estado {paciente.gravidade} acabou de ser registado no sistema, mas seu estado não era tão severo e por isso não entrou em nenhuma fila.")
            return
        if anuncio:
            self.logs.inserir(f"Um novo paciente({paciente}) de idade {paciente.idade} em estado {paciente.gravidade} acabou de ser registrado no sistema.")

        if paciente.f_etaria == 'n':
            if paciente.gravidade == 5:
                self.__nn_emerg__.inserir(paciente)
            elif paciente.gravidade == 4:
                self.__nn_m_urg__.inserir(paciente)
            elif paciente.gravidade == 3:
                self.__nn_p_urg__.inserir(paciente)
            else:
                return

            self.__total_nn__ += 1

        elif paciente.f_etaria == 'p':
            if paciente.gravidade == 5:
                self.__pd_emerg__.inserir(paciente)
            elif paciente.gravidade == 4:
                self.__pd_m_urg__.inserir(paciente)
            elif paciente.gravidade == 3:
                self.__pd_p_urg__.inserir(paciente)
            else:
                return
            self.__total_pd__ += 1

        elif paciente.f_etaria == 'a':
            if paciente.gravidade == 5:
                self.__ad_emerg__.inserir(paciente)
            elif paciente.gravidade == 4:
                self.__ad_m_urg__.inserir(paciente)
            elif paciente.gravidade == 3:
                self.__ad_p_urg__.inserir(paciente)
            else:
                return
            self.__total_ad__ += 1

    def alocarPacientes(self):
        """Remove os paciente com maior prioridade e os aloca no leito."""
        if not self.__leitos_nn__.vazia() and self.__total_nn__ > 0:
            while not self.__leitos_nn__.vazia() and self.__total_nn__ > 0:
                leito = self.__leitos_nn__.desempilhar()
                if not self.__nn_emerg__.vazia():
                    paciente = self.__nn_emerg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária neonatal em estado de emergencia foi alocado ao leito {leito} no hospital '{leito.hospital}'.")
                elif not self.__nn_m_urg__.vazia():
                    paciente = self.__nn_m_urg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária neonatal em estado de muita urgência foi alocado ao leito {leito} no hospital '{leito.hospital}'.")
                else:
                    paciente = self.__nn_p_urg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária neonatal em estado de urgência foi alocado ao leito {leito} no hospital '{leito.hospital}'.")

                self.__total_nn__ -= 1
                self.__tt_leitos_nn__ -= 1

        elif not self.__leitos_pd__.vazia() and self.__total_pd__ > 0:
            while not self.__leitos_pd__.vazia() and self.__total_pd__ > 0:
                leito = self.__leitos_pd__.desempilhar()
                if not self.__pd_emerg__.vazia():
                    paciente = self.__pd_emerg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária pediátrica em estado de emergencia foi alocado ao leito {leito} no hospital '{leito.hospital}'.")
                elif not self.__pd_m_urg__.vazia():
                    paciente = self.__pd_m_urg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária pediátrica em estado de muita urgência foi alocado ao leito {leito} no hospital '{leito.hospital}'.")
                else:
                    paciente = self.__pd_p_urg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária pediátrica em estado de urgência foi alocado ao leito {leito} no hospital '{leito.hospital}'.")

                self.__total_pd__ -= 1
                self.__tt_leitos_pd__ -= 1

        elif not self.__leitos_ad__.vazia() and self.__total_ad__ > 0:
            while not self.__leitos_ad__.vazia() and self.__total_ad__ > 0:
                leito = self.__leitos_ad__.desempilhar()
                if not self.__ad_emerg__.vazia():
                    paciente = self.__ad_emerg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária adulta em estado de emergencia foi alocado ao leito {leito} no hospital '{leito.hospital}'.")
                elif not self.__ad_m_urg__.vazia():
                    paciente = self.__ad_m_urg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária adulta em estado de muita urgência foi alocado ao leito {leito} no hospital '{leito.hospital}'.")
                else:
                    paciente = self.__ad_p_urg__.remover()
                    self.logs.inserir(f"Paciente({paciente}) da faixa etária adulta em estado de urgência foi alocado ao leito {leito} no hospital '{leito.hospital}'.")

                self.__total_ad__ -= 1
                self.__tt_leitos_ad__ -= 1

    def gerarFilaGeral(self):
        self.__fila_geral__.esvaziar()
        if self.__total_nn__ > 0:
            if not self.__nn_emerg__.vazia():
                self.__fila_geral__.mesclar(self.__nn_emerg__)
            if not self.__nn_m_urg__.vazia():
                self.__fila_geral__.mesclar(self.__nn_m_urg__)
            if not self.__nn_p_urg__.vazia():
                self.__fila_geral__.mesclar(self.__nn_p_urg__)
        if self.__total_pd__ > 0:
            if not self.__pd_emerg__.vazia():
                self.__fila_geral__.mesclar(self.__pd_emerg__)
            if not self.__pd_m_urg__.vazia():
                self.__fila_geral__.mesclar(self.__pd_m_urg__)
            if not self.__pd_p_urg__.vazia():
                self.__fila_geral__.mesclar(self.__pd_p_urg__)
        if self.__total_ad__ > 0:
            if not self.__ad_emerg__.vazia():
                self.__fila_geral__.mesclar(self.__ad_emerg__)
            if not self.__ad_m_urg__.vazia():
                self.__fila_geral__.mesclar(self.__ad_m_urg__)
            if not self.__ad_p_urg__.vazia():
                self.__fila_geral__.mesclar(self.__ad_p_urg__)

    def pacienteAleatorio(self) -> Paciente:
        """Função que retorna um paciente aleatorio dentre todas as filas."""
        self.gerarFilaGeral()
        limite_max = self.__fila_geral__.getTamanho()
        assert limite_max, "Tentativa de selecionar um paciente aleatório com filas vazias"

        indice_aleatorio = random.randrange(0, limite_max)

        for i in range(indice_aleatorio-1):
            self.__fila_geral__.remover()
        return self.__fila_geral__.remover()

    def removerPaciente(self, paciente: Paciente) -> Paciente:
        if paciente.f_etaria == 'n':
            if paciente.gravidade == 5:
                self.__nn_emerg__.removerEsp(paciente)
            elif paciente.gravidade == 4:
                self.__nn_m_urg__.removerEsp(paciente)
            elif paciente.gravidade == 3:
                self.__nn_p_urg__.removerEsp(paciente)

            self.__total_nn__ -= 1

        elif paciente.f_etaria == 'p':
            if paciente.gravidade == 5:
                self.__pd_emerg__.removerEsp(paciente)
            elif paciente.gravidade == 4:
                self.__pd_m_urg__.removerEsp(paciente)
            elif paciente.gravidade == 3:
                self.__pd_p_urg__.removerEsp(paciente)
            self.__total_pd__ -= 1

        elif paciente.f_etaria == 'a':
            if paciente.gravidade == 5:
                self.__ad_emerg__.removerEsp(paciente)
            elif paciente.gravidade == 4:
                self.__ad_m_urg__.removerEsp(paciente)
            elif paciente.gravidade == 3:
                self.__ad_p_urg__.removerEsp(paciente)
            self.__total_ad__ -= 1

        return paciente

    def pacientePiorou(self):
        paciente = self.pacienteAleatorio()
        if paciente.gravidade == 5:
            self.logs.inserir(f"Perdemos um paciente ({paciente}) de idade {paciente.idade} durante sua espera na fila.")
            self.removerPaciente(paciente)
            return

        self.logs.inserir(f"Paciente({paciente}) de idade {paciente.idade} piorou de {paciente.gravidade} para {paciente.gravidade+1}")
        paciente = self.removerPaciente(paciente)
        paciente.gravidade += 1
        self.novoPaciente(paciente, anuncio=False)

    def pacienteMelhorou(self):
        paciente = self.pacienteAleatorio()
        if paciente.gravidade == 3:
            self.logs.inserir(f"Paciente ({paciente}) de idade {paciente.idade} em estado '{paciente.gravidade}' melhorou para {paciente.gravidade-1} e não precisa mais estar na fila.")
            self.removerPaciente(paciente)
            return

        self.logs.inserir(f"Paciente({paciente}) de idade {paciente.idade} melhorou de {paciente.gravidade} para {paciente.gravidade-1}")
        paciente = self.removerPaciente(paciente)
        paciente.gravidade -= 1
        self.novoPaciente(paciente, anuncio=False)


if __name__ == "__main__":
    sim = Simulador("Teste")

    print(sim)

    sim.novoPaciente(Paciente(0, 3))
    sim.novoPaciente(Paciente(10, 4))
    sim.novoPaciente(Paciente(20, 5))
    sim.pacientePiorou()

    print(sim)
