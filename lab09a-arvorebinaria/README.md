[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9194017&assignment_repo_type=AssignmentRepo)
# Lab09 - Árvores Binárias

Nesse Lab voce encontra uma implementação do **TAD Árvore Binária**. 

A construção da **árvore** foi feita a partir de uma sequência de chaves arbitrária. O critério que guia esse processo é distribuir igualmente entre cada **sub-árvore** um número igual de **nós**. 

O algoritmo recebe o numero total de **nós** a serem distribuidos em sua primeira chamada. A partir dai cria uma raiz para a **sub-árvore**, e calcula quantos **nós** restam para cada uma das **sub-árvore**s esquerda e direita usando uma simples relação matemática:
 
> 	nnd = n // 2 			# numero de nós da sub-árvore direita
> 	nne = n - nnd - 1 		# numero de nós da sub-árvore esquerda

sendo `n` o número de nós da **sub-árvore** em questão. Ou seja, metade dos **nós** da **sub-árvore** que esta sendo construida irão para a **sub-árvore** direita e o numero de nós restante (`n - nnd`) descontado o **nó** alocado a raiz (-1) irão para a **sub-árvore** esquerda. 

O código em *Python* da função que monta recursivamente a **árvore** é:

>
>  def __MontaAB__(self, n):
>
>		  if n == 0:
>			  return None;
>
>		  novoNo = cNo.cNo(self.chave);
>		  self.chave += 1 
>
>		  if novoNo == None:
>			  return novoNo
>
>		  self.__numNos__ += 1
>
>		  nnd = n // 2
>		  nne = n - nnd - 1
>
>		  novoNo.setFilhoEsq(self.__MontaAB__(nne))
>		  novoNo.setFilhoDir(self.__MontaAB__(nnd))
>
>		  return novoNo

# Referências Bibliográficas:

Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012..

Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.

