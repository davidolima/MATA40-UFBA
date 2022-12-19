import random as r
import sys

def imprimirPlaca(palavra, tam):  # Função para imprimir uma placa grande no console com uma dada palavra
    meio = '|' + ' ' * (tam // 2 + len(palavra) // 2) \
           + palavra \
           + ' ' * (tam // 2 + len(palavra) // 2) + '|'
    print('-' * len(meio))
    print(meio)
    print('-' * len(meio))

# Função para comparar minha ordenação com a ordenação do python. Imprime a % de acertos.
def compararOrdenacao(p, l):
    #l.reverse()
    acertos = 0
    for i in range(len(l)):
        if p[i] == l[i]:
            print('\033[92m'+ l[i] + '\033[0m', end=' ')
            acertos += 1
        else:
            print('\033[91m'+ l[i] + '\033[0m', end=' ')
    print(f'\n>> Acurácia: {acertos*100/len(l)}%\n')

def gerarPlacas(n=10, nome_do_arquivo="placas.txt"):
    ALFA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    with open(nome_do_arquivo, "w+") as f:
        for i in range(n):
            f.writelines(r.choice(ALFA)+
                         r.choice(ALFA)+
                         r.choice(ALFA)+
                         str(r.randrange(0,9))+
                         r.choice(ALFA)+
                         str(r.randrange(0,9))+
                         str(r.randrange(0,9))+
                         '\n')

if __name__ == "__main__":
    nome_do_arquivo = "placas.txt"
    n = 10

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    if len(sys.argv) > 2:
        nome_do_arquivo = sys.argv[2]

    gerarPlacas(nome_do_arquivo, n)
    print(n, 'placas geradas no arquivo "'+ nome_do_arquivo +'".')