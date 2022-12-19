# Relatório Técnico
---
### MATA40 - Estrutura de Dados e Algoritmos I
### Prof. Antonio Lopes Apolinario Junior
### Aluno: David de Oliveira Lima
---

> O algoritmo que escolhi para a resolução do nosso problema foi o ***Radix Sort*** (Ordenação digital).

## A Escolha do Algoritmo
O *Radix Sort* foi escolhido devido a algumas de suas características e capacidades:
 1. A possibilidade de implementar paralelismo[3][4], que poderemos utilizar para aproveitar o grande poder de processamento dos datacenters onde nosso algoritmo será executado.
 2. A sua eficiência, onde seu caso médio é `O(d(n + k))`[1] (Sendo **k** o número de valores possíveis de cada dígito, **d** a quantidade de dígitos e **n** a quantidade de entradas). Como nossa base de dados tem uma quantidade de caracteres (d = 7) e valores possíveis de cada dígito constantes (k = 36), nosso algoritmo apresenta complexidade de `O(n)`.
 3. A sua compatibilidade com a ordenação Lexicográfica[3], pois o algoritmo funciona de uma forma similar a esse tipo de ordenação (Ordena por caractere/algarismo).
 4. Apesar da implementação ter sido feita com uma lista encadeada, como o algoritmo só precisa passar uma vez pelos dados, pode-se utilizar qualquer TAD para sua implementação.

# A Implementação
A Implementação do algoritmo foi realizada utilizando uma classe customizada, baseada em Listas Encadeadas como tipo abstrato de dados. Além disso criei algumas funções auxiliares para uma apresentação e um desenvolvimento mais prazeroso. O algoritmo foi uma adaptação [deste](https://pt.wikipedia.org/wiki/Radix_sort#C%C3%B3digo_em_Python) código. Foi modificado para realizar a intregração do meu TAD e da minha função *valorASCIINorm*, além de adaptá-lo para o problema.

# Organização de arquivos
Existem alguns arquivos com funções para auxílio no desenvolvimento, com dito anteriormente. As funções auxiliares criadas no arquivo **funçõesAuxiliares.py**, dentre elas existem:
 - *gerarPlacas*: Uma função para gerar *n* PIVs, para não precisar testar o algoritmo na enorme base de dados. 
 - *imprimirPlaca*: Uma função para imprimir uma placa no console, apenas por estética.
 - *compararListas*: Uma função que compara duas listas e retorna a similaridade entre elas, para eu comparar a minha organização com a organização do *sorted()* do python e acompanhar se o algoritmo está retornando os resultados esperados.
 
 Além disso, temos:
 - O arquivo **main.py** que contém a função principal.
 - O arquivo **TADs.py** que contém a implementação do Nó e da Lista Encadeada.
 - O arquivo **radixSort.py** que contém a implementação do algoritmo escolhido.

 # Utilizando a função principal
 Para utilizar a função principal na base de dados disponibilizada pelo professor, execute o comando `python3 main.py p`. Alternativamente, escolha a quantidade de dados do dataset com o comando `python3 main.py p <n>`, sendo que \<n\> pode ser 10000, 100000 ou 1000000.
 
 Para gerar uma quantidade \<n\> de placas aleatórias e passá-las pelo algoritmo, utilize o comando `python3 main.py r <n>`.
 
 Para executar o algoritmo em 10 placas aleatórias, simplesmente chame o interpretador no arquivo principal: `python3 main.py`.

# Referências Bibliográficas
---
[1] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012.

[2] Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.

[3] **Radix Sort**. https://en.wikipedia.org/wiki/Radix_sort

[4] **Radix Sort Algorithm in Data Structure**. https://www.scaler.com/topics/data-structures/radix-sort/

[5] **Types and Objects in Python**. https://www.informit.com/articles/article.aspx?p=453682&seqNum=6
