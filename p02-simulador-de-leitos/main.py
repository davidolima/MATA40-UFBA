#!/usr/bin/env python3

from cSimulador import Simulador
from cPaciente import Paciente
import random
import funcAux

def interpretarComando(comando):
    if comando.startswith('pm'):
        sim.pacienteMelhorou()
        return funcAux.traduzirComando(comando)
    elif comando.startswith('pp'):
        sim.pacientePiorou()
        return funcAux.traduzirComando(comando)

    if comando.startswith('la'):
        evento, idade = comando.split()
        if idade.isnumeric():
            idade = funcAux.faixaEtaria(int(idade))
        elif idade == 'r':
            idade = random.choice(('n', 'p', 'a'))
            comando = comando.replace('r', idade, 1)

        sim.novoLeito(idade)
        return funcAux.traduzirComando(comando)

    else:
        evento, idade, gravidade = comando.split()
        if idade == 'r':
            idade = funcAux.gerarIdadeAleatoria()
            comando = comando.replace('r', str(idade), 1)
        if gravidade == 'r':
            gravidade = random.randrange(1, 6)
            comando = comando.replace('r', str(gravidade), 1)
        gravidade = int(gravidade)

    idade = int(idade)

    paciente = Paciente(idade, gravidade)
    sim.novoPaciente(paciente)

    return funcAux.traduzirComando(comando)

def interface():
    global sim
    funcAux.cabecalho()

    # Iniciar simulador
    sim = Simulador()

    while True:
        prompt = input("\nInsira um evento ou pressione enter:")
        if prompt == 's' or prompt == 'q' or prompt == 'quit' or prompt == 'sair':
            break
        elif prompt == 'h' or prompt == 'help' or prompt == 'a' or prompt == 'ajuda':
            funcAux.instrucoes()
            continue
        elif prompt == 'st' or prompt == 'status'or prompt == 'e' or prompt == 'estado':
            print(sim)
        elif prompt.startswith('la') or prompt.startswith('pp') or prompt.startswith('pm') or prompt.startswith('np'):
            sim.alocarPacientes() # O simulador vai antes de todos os ciclos tentar alocar pacientes para os leitos disponíveis
            sim.gerarFilaGeral()
            if (prompt.startswith('pp') or prompt.startswith('pm')) and sim.__fila_geral__.vazia():
                print("\n[!] Só é possível utilizar os comandos de piora ou melhora de pacientes quando existem pacientes nas filas. Tente novamente.")
                continue
            comando_traduzido = interpretarComando(prompt)

        elif not prompt:
            sim.alocarPacientes() # O simulador vai antes de todos os ciclos tentar alocar pacientes para os leitos disponíveis
            prompt = funcAux.eventoAleatorio(sim)
            comando_traduzido = interpretarComando(prompt) # Interpretar comando e enviar pro simulador

        elif prompt[0].isnumeric():
            x = prompt.split()
            if len(x) > 1: # Se existir algum comando para repetir
                for i in range(int(x[0])): # repetir o comando n vezes
                    comando = str(x[1:]).replace("', '", ' ').replace("['","").replace("']",'')
                    comando_traduzido = interpretarComando(comando) # Interpretar comando e enviar pro simulador
            else:
                for i in range(int(x[0])): # gerar n comandos aleatorios
                    comando = funcAux.eventoAleatorio(sim)
                    comando_traduzido = interpretarComando(comando) # Interpretar comando e enviar pro simulador
                    sim.alocarPacientes()

            sim.alocarPacientes() # O simulador vai antes de todos os ciclos tentar alocar pacientes para os leitos disponíveis

        else:
            print("\nComando inválido! Digite 'h' / 'help' / 'a' / 'ajuda' para obter ajuda.")

        print(sim)
        print("\nEvento:")

        print(prompt, "->", comando_traduzido)

if __name__ == "__main__":
    interface()
