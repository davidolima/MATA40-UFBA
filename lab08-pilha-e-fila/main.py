from cPilha import Pilha
from cFila import Fila

def testarPilha(pilha):
    print('-----------------')
    print('Testando empilhar')
    print('-----------------')

    for i in range(0, 10, 3):
        pilha.empilhar(i)
    print(pilha)

    print('--------------------')
    print('Testando desempilhar')
    print('--------------------')

    while not pilha.vazia():
        pilha.desempilhar()

    print(pilha)

def testarFila(fila):
    print('-------------------')
    print('Testando enfileirar')
    print('-------------------')

    for i in range(0, 10, 3):
        fila.enfileirar(i)
    print(fila)

    print('-----------------------')
    print('Testando desenfileirar')
    print('-----------------------')

    while not fila.vazia():
        fila.desenfileirar()
    print(fila)


if __name__ == "__main__":
    p = Pilha()
    testarPilha(p)

    f = Fila()
    testarFila(f)
