from TADs import ListaEnc  # Importar meu TAD
from funçõesAuxiliares import * # Importar algumas funções customizadas para testes e conveniência
from radixSort import radixSort # Importar o algoritmo de sort

import sys  # Para trocar entre os dados do professor e os gerados aleatoriamente através da CLI

def executar(qtd_entradas, metodo):
    placas = ListaEnc()

    # Importar placas #
    if metodo == 'r': # Utilizar o gerador de placas ou utilizar os datasets do professor
        gerarPlacas(qtd_entradas) # gerar n (qtd_entradas) placas aleatórias

        with open("placas.txt", 'r') as f:  # Ler placas na memória
            for placa in f.readlines():
                placas.inserir(placa[:-1])  # placa[:-1] para remover o '\n'
                
    elif metodo == 'p':
        with open(f"PIVs-{qtd_entradas}.piv", 'r') as f: # Ler placas na memória
            for placa in f.readlines():
                placas.inserir(placa[:-1])  # placa[:-1] para remover o '\n'

    # Output #
    if len(placas) < 1000:
        imprimirPlaca("Original", 30)
        print(placas,end='\n\n')

        radixSort(placas)

        imprimirPlaca("Ordenado", 30)
        print(placas,end='\n\n')

    else:
        radixSort(placas)

    imprimirPlaca("Acurácia", 30)
    compararOrdenacao(placas, sorted(placas)) # VETOR ORDENADO COM SORTED PARA COMPARAÇÃO

if __name__ == "__main__":
    qtd_entradas = 10
    metodo = 'r'

    # Administrar argumentos da linha de comando #
    if len(sys.argv) > 1:
        metodo = sys.argv[1]

    if metodo == 'r':
        qtd_entradas = 10
    else:
        qtd_entradas = 10000

    if len(sys.argv) > 2:
        qtd_entradas = int(sys.argv[2])

    executar(qtd_entradas, metodo) # Executar Algoritmo
    
    