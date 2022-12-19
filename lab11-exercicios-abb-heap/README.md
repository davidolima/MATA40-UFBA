[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9398609&assignment_repo_type=AssignmentRepo)
# Lab11 - Exercícios Árvore Binária de Busca & Heap

I. Extenda o código discutido nas aulas, que implementa uma **Árvore Binária de Busca**, acrescentando os seguintes métodos:

1. Calcula o número de nós de uma sub-árvore (dada sua raiz);
2. Calcula a altura de uma sub-árvore (dada sua raiz);
3. Conta quantas folhas existem em uma sub-árvore (dada a sua raiz);
4. Imprimir as chaves da **ABB** em ordem crescente e decrescente;
5. Percorre a árvore em largura, ou seja, imprima seus nós por nível, da esquerda para a direita, na ordem em que eles aparecem.

>A maioria desses algoritmos se valerão da definição recursiva de árvore e usaram a recursividade para resolver o problema. Mas nem todos. Por isso fique atento. 

II. Analise se é possível implementar os algoritmos de percurso básicos sem utilizar recursão. Em caso afirmativo, implemente sua solução e teste seu resultado. 

III. Modifique a sua classe **Arvore Binária de Busca** para que seja possivel, dada raiz de outra árvore, verificar se as duas árvores são identicas.

IV. Modifique a sua classe **Arvore Binária de Busca** para que, dada a raiz de outra árvore, promova o *merge* das duas árvores. Ao final a segunda árvore deverá estar vazia.

V. Crie uma nova classe **Arvore Binária de Busca** que:

1. Mantenha em cada nó uma referencia ao nó pai;
1. Mantenha em cada nó a altura da sub-arvore associada;

>Lembre-se de que essas novas informações devem ser mantidas consistentes, portanto, podem induzir mudanças em diversos métodos da nova classe. 

VI. Construa uma classe que implementa um **Heap**. 

1. Sua classe deve receber no construtor a indicação se o **Heap** será um **maxHeap** ou um **minHeap**. E controlar o processo de inserção e remoção de chaves de modo adequado em função dessa escolha (que não pode mudar ao longo do tempo de vida do **Heap**).

VII. Encontre o **k-ésimo** maior elemento de um conjunto. Para tanto pense em estratégias utilizando:

1. Um **minHeap**
2. Um **maxHeap**

Analise a complexidade de cada uma das soluções. Qual a mais eficiente? 

VIII. Sobre **Heaps** responda e justifique:

1. Onde em um **minHeap** de inteiros deve estar a maior das chaves? (assuma que todos as chaves são distintas)
2. Qual a máxima e mínima quantidade de chaves que podem ser armazenadas em um **Heap** de altura  *h*.
3. Suponha que ao invés de um **heap binário** nós queremos trabalhar com um **heap ternário**. Qual seria o esquema de indexação a ser utilizado para que os nós da árvore formem uma sequencia contínua? Considere que a raiz tem índice 0.  Mostre como seria esse esquema de índices para um **heap ternário** com 12 chaves.  
