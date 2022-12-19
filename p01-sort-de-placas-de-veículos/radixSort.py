from TADs import ListaEnc  # Importar meu TAD

def valorASCIINorm(x):  # Função para retornar um valor entre 0 e 36 para usarmos no counting sort
    try:
        x = int(x) # transformar digitos do tipo "d" em d
    except:
        pass
    if isinstance(x, str):
        return ord(x) - 54
    else:
        return x

def radixSort(lista):
    N_CARACTERES = 26 + 10 # espaço para 10 números (0-9) e 26 letras (A-Z)

    for casa in range(6, -1, -1): # começando de 6, pois é o maior índice dentro de uma PIV
        # Criar n grupos para classificação das placas, onde n é o número de caracteres possíveis de se encontrar (0-9^A-Z)
        grupos = [ListaEnc() for i in range(N_CARACTERES)]
        for placa in lista:
            indice = valorASCIINorm(placa[casa])
            grupos[indice].inserir(placa) # Inserir placa no seu respectivo grupo, relacionado ao caractere naquela casa
        
        lista.esvaziar()
        lista = sum(grupos, lista.__iter__()) # Salvar estado da lista

    return lista