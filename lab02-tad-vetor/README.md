[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8344136&assignment_repo_type=AssignmentRepo)
# Lab 02 - Implementando um TAD Vetor

Nesse Lab voce deve tentar implementar um **Tipo Abstrato de Dados** (**TAD**) *vetor*, utilizando o conceito de *Classe* da linguagem *Python*.

Um vetor deve ser caracterizado por ser um agregado de objetos do mesmo tipo, com suporte as seguintes operações básicas:

1. **Criar**: nessa operação o tamanho máximo do vetor deve ser definido. Ao longo de todas as demais operações esse tamanho deve ser mantido e verificado;
2. **Imprimir**: Gera uma saida formatada de todos os elementos do vetor;
3. **Inserir**: Adiciona um novo objeto ao vetor, como ultimo elemento;
4. **Buscar**: Procura nos elementos do vetor se existe algum objeto que possua valor igual ao da chave de busca, retornando a sua primeira ocorrencia. A operação deve sinalizar de alguma forma se a busca obteve ou não sucesso; 
5. **Remover**: Elimina do vetor a primeira ocorrencia do objeto com valor igual ao da chave de remoção. A operação deve sinalizar de alguma forma se a busca obteve ou não sucesso;  
6. **Tamanho**: Operação que retorna o numero de elementos atualmente armazenado no vetor;
7. **Minimo**: Retorna a menor valor armazenado no vetor;
8. **Maximo**: Retorna o maior valor armazenado no vetor;
9. **Ocorrências**: Dada uma chave, a operação retorna o numero de ocorrências dessa chave no vetor;
10. **E_Identico**: Essa operação compara dois vetores (o próprio e outro passado como parametro) e retorna um valor booleano sinalizando se os dois vetores são ou não identicos;
11. **Inverter**: Troca a ordem dos elementos do vetor;
12. **GerarEstatisticas**: calcula média, desvio padrão e mediana do conjunto.

O **TAD**/*Classe* *vetor* deve ser codificado como um módulo em *Python*. Para testar seu **TAD** voce deve criar um programa de teste que avalie as operações que voce implementou. 
