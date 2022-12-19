[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8512723&assignment_repo_type=AssignmentRepo)
# Lab04 - Algoritmos de Busca e Ordenação

Nesse Lab vamos analisar os algoritmos de *Busca e Ordenação*.

No código fornecido voce encontra a implementação dos algoritmos de **Busca Sequencial** e **Busca Binária**, sendo esse ultimo implementado em suas versões iterativa e recursiva.

O módulo principal gera um vetor com valores aleatórios e simula diversas buscas, computando algumas estatísticas desses algoritmos, como número mínimo (melhor caso), máximo (pior caso) e médio de comparações executas. Ao final do processo a média desses valores é comparada aos valores teoricos esperados dadas as complexidades dos respectivos algoritmos. 

1. Analise com bastante cuidado como o programa funciona. Execute com diferentes valores de tamanho do vetor (passando como parametro na linha de comando) e compare se os valores "reais" batem com o numero esperado na complexidade. 

2. Para os testes da **Busca Binária** aproveitamos o algoritmo de ordenação, fornecido pela implementação de vetores do próprio *Python* (linha 126 do modulo *cVetor.py*). Sua tarefa nesse Lab será implementar diferentes algoritmos e promover o mesmo tipo de analise feita para a busca. Ou seja, tentar executar várias vezes a ordenação e calcular os valores reais e os estimados pela teoria. Os algoritmos de ordenação que voce deve testar são:

	a. por Seleção

	b. por Inserção 

	c. Método da Bolha (Bubble Sort) [^1]

	d. Quicksort [^2]

	e. Merge Sort [^3]

Para compreender de forma inituitiva o funcionamento de cada um desses algoritmos, acesse: 

https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html

e compare os métodos. Caso tenha duvidas, consulte o professor ou o monitor do Lab. 

# Referencias Bibliográficas:

- Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. Algoritmos – Teoria e Prática. Editora Campus. 3a Edição, 2012..

- Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 


[^1]: https://www.cos.ufrj.br/~rfarias/cos121/aula_05.html

[^2]: https://www.cos.ufrj.br/~rfarias/cos121/aula_08.html

[^3]: https://www.cos.ufrj.br/~rfarias/cos121/aula_07.html
