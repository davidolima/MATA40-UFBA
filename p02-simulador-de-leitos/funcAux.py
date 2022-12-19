import random

def instrucoes():
    print("-=-=-=-=-=-=-=-=-=-=-")
    print("        AJUDA       ")
    print("-=-=-=-=-=-=-=-=-=-=-")

    print("--------------------")
    print("|   Como Funciona  |")
    print("--------------------")
    print("Você pode:")
    print(" - Apertar [Enter] para a simulação gerar um evento aleatório.")
    print(" - Inserir um número para gerar e executar n eventos simultâneos.")
    print(" - Inserir um evento no terminal para testar a simulação.")
    print(" - Inserir um número seguido de um evento para executá-lo n vezes.")

    print("\n------------------------------------")
    print("| Estrutura dos eventos & Comandos |")
    print("------------------------------------")
    print("\n~> Tipos de Eventos")
    print("  => 'la' para indicar que um leito foi disponibilizado.")
    print("  => 'pp' para indicar que algum paciente piorou.")
    print("  => 'pm' para indicar que algum paciente melhorou.")
    print("  => 'np' para adicionar um novo paciente de idade [Idade] e gravidade [Severidade].")
    print("  => 'q' / 'quit'/ 's' / 'sair' para sair do simulador.")
    print("  => 'h' / 'help' / 'a' / 'ajuda' para mostrar este guia. ")
    print("  => 'st' / 'status' / 'e' / 'estado' para ver o estado das filas.")
    print("\n~> Idades")
    print("  => 'n' para Neonatal")
    print("  => 'p' para Pediátrico")
    print("  => 'a' para Adulto")
    print("  => 'r' para uma escolha aleatória")
    print("\n~> Severidade")
    print("  => '5' para Emergência")
    print("  => '4' para Muito urgente")
    print("  => '3' para Urgente")
    print("  => '2' para Pouco urgente")
    print("  => '1' para Não urgente")
    print("  => 'r' para uma escolha aleatória")
    print("\n~>EXEMPLOS")
    print("  => 'la p'      = Um leito para pacientes de idade pediátrica foi disponibilizado.")
    print("  => 'pp'        = Algum paciente piorou.")
    print("  => 'np p 5'    = Chegou um novo paciente de faixa etária pediátrica de gravidade 5 (Emergência).")
    print("  => '20 la a'   = Repetir o comando 'la a' 20 vezes.")
    print("  => '20'        = Gerar e executar 20 comandos aleatórios.")
    print("  => '10 np r r' = Executar 'np' 10 vezes com idades e gravidades aleatórias.")
    print("-=-=-=-=-=-=-=-=-=-=")


def traduzirComando(comando):
    """
    Função para tornar a leitura de comando mais simples para o usuário.
    """

    eventos = {'la': "Leito aberto para a faixa etária [idade]",
               'pp': "Algum paciente piorou.",
               'pm': "Algum paciente melhorou.",
               'np': "Novo paciente [idade] em estado de [gravidade]"}
    idades = {'n': "neonatal", 'p': "pediatrico", 'a': "adulto"}
    gravidades = {5: "emergencia",     4: "muita urgencia", 3: "urgencia",
                  2: "pouca urgencia", 1: "não urgencia",  '': ''}


    comando = comando.split()
    evento = comando[0]
    if evento == 'pm' or evento == 'pp':
        return eventos[evento]

    try:
        idade = int(comando[1])
        if idade == 0:
            f_etaria = 'n'
        elif 1 <= idade <= 13:
            f_etaria = 'p'
        elif 13 < idade:
            f_etaria = 'a'
    except:
        idade = comando[1]
        f_etaria = idade

    gravidade = ''
    if evento == 'np':
        gravidade = int(comando[2])
        return eventos[evento].replace("[idade]",idades[f_etaria] + f"({idade})").replace("[gravidade]",gravidades[gravidade])
    elif evento == 'la':
        return eventos[evento].replace("[idade]",idades[f_etaria] + f"({idade})")


def eventoAleatorio(sim):
    sim.gerarFilaGeral()
    if sim.__fila_geral__.vazia():
        evento = random.choice(('np', 'la'))
    else:
        evento = random.choice(('np', 'pm', 'pp', 'la'))

    idade = gerarIdadeAleatoria()

    if evento == 'np':  # Comandos que requerem input de gravidade
        gravidade = random.randrange(1, 6)
        return evento + ' ' + str(idade) + ' ' + str(gravidade)
    elif evento == 'la':
        return evento + ' ' + str(idade)
    else:
        return evento

def gerarIdadeAleatoria():
    idade = random.randrange(0, 3)
    if idade == 1:
        idade = random.randrange(1, 13)
    elif idade == 2:
        idade = random.randrange(14, 70)
    return idade

def faixaEtaria(n):
   if n == 0:
       return 'n'
   elif 1 <= n <= 13:
       return 'p'
   elif 13 < n:
       return 'a'

def cabecalho():
    print("-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-")
    print("              Simulador de Leitos")
    print("             David de Oliveira Lima")
    print(" UFBA - Prof. Antonio Lopes Apolinario Junior ")
    print("-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=-")
    print("\nDigite 'h' / 'help' / 'a' / 'ajuda' para obter ajuda.")
