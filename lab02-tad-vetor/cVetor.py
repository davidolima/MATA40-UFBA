# Desafio pessoal: Não utilizar append
class Vetor:
    tamanho = 0
    lista = []

    def __init__(self, tamanho: int, *elementos):
        self.tamanho = tamanho
        self.lista = [0] * tamanho # aloca o espaço necessário para os elementos
        if elementos:
            for i in range(tamanho):
                self.lista[i] = elementos[i]

    def tam(self): # Tamanho
        return self.tamanho

    def __str__(self):  # print(vetor), Imprimir
        string = ''
        for elemento in self.lista:
            string += str(elemento) + ", "
        string = string[:-2]
        return '<'+string+'>'

    def __repr__(self): # Representação mais bonitinha
        return self.__str__()

    def __getitem__(self,indice): # Vetor[n] = n-eśimo elemento, Acessar item
        return self.lista[indice]

    def inserir(self, elemento): # Criar
        self.lista += [elemento]
        self.tamanho += 1

    def remover(self, elemento): # Remover
        self.lista.remove(elemento)
        self.tamanho -= 1

    def busca(self, elemento): # Busca
        for i in range(self.tamanho):
            if self.lista[i] == elemento:
                return i
        return -1

    def minimo(self): # Minimo
        min = self.lista[0]
        for i in self.lista:
            if min > i:
                min = i
        return min

    def maximo(self): # Maximo
        max = self.lista[0]
        for i in self.lista:
            if max < i:
                max = i
        return max

    def ocorrencias(self, elemento): # Ocorrencias
        contagem = 0
        for i in self.lista:
            if i == elemento:
                contagem += 1
        return contagem

    def __eq__(self, other): # Vetor A == Vetor B, E_identico
        if isinstance(other, Vetor):
            if other.tamanho != self.tamanho:
                return False
            for i in range(self.tamanho-1):
                if other.lista[i] != self.lista[i]:
                    return False
            return True

    def inverter(self): # Inverter
        inverso = []
        for i in range(self.tamanho-1, -1, -1):
            inverso += [self.lista[i]]
        return inverso

    def soma(self): # Funcao auxiliar para a media e o desvio padrao
        r = 0
        for i in self.lista:
            r += i
        return r

    def media(self): # Calcula a média
        return self.soma() / self.tamanho

    def mediana(self): # Retorna a mediana
        if self.tamanho % 2 == 1:
            return self.lista[self.tamanho // 2]
        else:
            return (self.lista[self.tamanho // 2] + self.lista[(self.tamanho // 2) - 1]) / 2

    def desvioPadrao(self): # Calcula o desvio padrão
        media = self.media()
        desvios = Vetor(self.tamanho) # usando o próprio TAD para calcular o desvio padrao!
        for x in self.lista:
            desvios.inserir((x-media)**2)
        s = desvios.soma()
        dp = (s / self.tamanho)**(1 / 2)
        return dp

    def estatisticas(self): # GerarEstatisticas
        return self.media(), self.desvioPadrao(), self.mediana()
