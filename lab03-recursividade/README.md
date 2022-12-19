[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8418614&assignment_repo_type=AssignmentRepo)
# Lab 03 - Recursividade

# Fundamentação Teórica:

Procedimentos recursivos são uma forma bastante interessante e elegante de resolver problemas. O que caracteriza um procedimento ou função recursiva é que ela é "resolvida" a partir da solução de instâncias menores do próprio problema. O processo de "redução" do problema é feito até que se encontre um problema elementar ou "infantil", cuja solução é conhecida ou é muito simples e pode ser obtida sem o uso da recursividade. 

Vejamos o exemplo do código fonte fornecido nesse Lab para o calculo do valor do *Fatorial* de um valor *n*, que é definido como:

>fat(n) = n * (n-1) * (n-2) * (n-3) * .... * 3 * 2 * 1

Percebe-se claramente por essa definição que o problema possui uma solução iterativa simples:

``` 

	def fatorial(n):

	    if n < 0:
	        return None 

	    if n == 0:
	        return 1

	    fat = 1

	    for i in range(1, n+1):
	        fat = fat * i

	    return fat 

``` 

Porém analisando com mais cuidado a definição da função *fat(n)* percebe-se que ela pode ser re-escrita como:

>fat(n) = n * (n-1) * (n-2) * (n-3) * .... * 3 * 2 * 1 =
>       = n * fat(n-1)

Essa nova relação não resolve diretamente a função *fat(n)* mas a define a partir de um problema menor *fat(n-1)*. Seguindo essa lógica: 

>fat(n-1) = (n-1) * fat(n-2)
>
>fat(n-2) = (n-2) * fat(n-3)
>
>fat(n-3) = (n-3) * fat(n-4)
>
>.....
>
>fat(3)   = 3 * fat(2)
>
>fat(2)   = 2 * fat(1)
>
>fat(1)   = 1 * fat(0)
>
>fat(0)   = 1

Como podemos perceber, quando chegamos a função *fat(0)* não faz sentido continuar o processo recursivo pois a função fatorial só é definida para valores inteiros positivos. Porém sabemos que, por definição, *fat(0) = 1*. Esse, portanto, é nosso problema elementar ou "infatil" onde o processo recursivo não é mais aplicado e temos uma solução conhecida. 

A partir de agora, podemos retornar aos problemas anteriores (que ficaram sem solução) e resolve-los:

>fat(0)   = 1
>
>fat(1)   = 1 * fat(0) = 1 * 1 = 1 
>
>fat(2)   = 2 * fat(1) = 2 * 1 = 2
>
>fat(3)   = 3 * fat(2) = 3 * 2 = 6
>
>fat(4)   = 4 * fat(3) = 4 * 6 = 24
>
>fat(5)   = 5 * fat(4) = 5 * 24 = 120
>....

Até alcançarmos o valor de *fat(n)*. 

Dessa forma, fica claro que uma função recursiva vai sempre possuir dois elementos: 

1. Identifição do problema elementar e o retorno de sua solução direta;
2. A redução do problema e a chamada da função de forma recursiva, passando como parametro o problema reduzido.

Re-escrevendo a função *Fatorial* de forma recursiva, temos:

``` 

	def fatorialRec(n):

	    if n == 0:
	        return 1

	    return n * fatorialRec(n-1)

```

Para por alguns instantes, reflita sobre tudo o que foi colocado aqui. 

# Exercícios:

Agora que voce já deve ter entendido, pelo menos conceitualmente, o que é recursão, vamos a algumas tarefas práticas para exercitar o conceito!!

1. Modifique o exemplo *fatorial.py* incluindo *print's*  para que voce possa acompanhar o processo recursivo (tipo "entrei na função", "testei o problema infantil", "vou fazer a chamada recursiva", retornei da chamada recursiva"). Para acompanhar o processo voce deve indicar nesses *print's* qual o valor de *n* a função está calculando naquele momento.

2. Faça um programa em *Python* que calcule o valor de um numero *n* elevado a potencia *e*. Tal como no exemplo do *Fatorial* codifique uma função interativa e uma função recursiva para resolver o mesmo problema.
**Sugestão:** construa a formula de *pot(n)* e depois procure escrever sua forma recursiva.

3. Faça um programa em *Python* que calcule o somatório dos *n* inteiros, no intervalo [1..n], utilizando uma função recursiva.

4. Faça um programa em *Python* que calcule o valor do n-ésimo termo da *Série de Fibonacci*[^1], que é definida por:

[<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/4fa6d281e7a54e08aeffeef7458ddc0884333686">](http://google.com.au/)

onde:

[<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/3c667d91153450b3a161371582ee8227af85951f">]() 

5. Faça um programa em *Python* que gera todos os anagramas de uma palavra fornecida como parâmetro. Por exemplo, para a palavra "lago", seu programa deve gerar como saída a seguinte sequencia de palavras (não necessáriamente nessa mesma ordem):

> Anagramas de lago = 
> ['lago', 'algo', 'aglo', 'agol', 'lgao', 
> 'glao', 'galo', 'gaol', 'lgoa', 'gloa', 
> 'gola', 'goal', 'laog', 'alog', 'aolg', 
> 'aogl', 'loag', 'olag', 'oalg', 'oagl', 
> 'loga', 'olga', 'ogla', 'ogal'] 

Use uma função recursiva para resolver esse problema.

# Desafio do final de semana:

Se voce chegou até aqui e acha que já esta dominando recursividade, e quer ter o que pensar no final semana, aqui vão alguns desafios:

Analise com bastante cuidado o programa *cantorSet.py* fornecido nesse Lab. Ele vai utilizar a biblioteca *PyGlet*[^2] para a parte gráfica. 

Esse programa gera um conjunto conhecido como *Conjunto de Cantor*[^3]. Sua definição é baseada em uma relação recursiva de construção: a partir de um segmento de reta, remove-se seu terço interno, gerando 2 segmentos (primeiro terço e último terço). O processo é repetido sempre para os novos segmentos. O conjunto formado pela repetição desse processo, quando ele tende ao infinito possui diversar propriedades matemáticas interessantes. Mas para nós é interessante analisar o processo recursivo utilizado na função *desenhaCurva()* do código. Analise e tente entender como as linhas são geradas e desenhadas. 

Uma vez entendido o código base:

1. Modifique o programa para que desenhe apenas o último nível do conjunto.

2. Utilizando um processo construitivo semelhante, outras curvas podem ser criadas como a *Curva de Koch* ou "Floco de Neve"[^4]. Modifique o programa *cantorSet.py* para gerar essa curva.

[<img src="https://i.stack.imgur.com/GTl2s.png">]() 

3. Uma fractal bastante conhecido e que também segue um processo recursivo de definição é o *Triangulo de Sierpinsky* [^5]. Modifique o programa *cantorSet.py* para gerar essa fractal.

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/SierpinskiTriangle.PNG/640px-SierpinskiTriangle.PNG">]() 

[^1]: https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci

[^2]: https://pyglet.org/

[^3]: https://en.wikipedia.org/wiki/Cantor_set

[^4]: https://en.wikipedia.org/wiki/Koch_snowflake

[^5]: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
