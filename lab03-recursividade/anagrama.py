###############
# lago - > fixa uma letra "l"
# laog - > fixa a segunda letra "a" e troca as restantes
# lgao - > troca a segunda letra fixa
# lgoa - > troca as restantes
# loag - > troca a segunda letra fixa
# loga - > troca as restantes. Fim das possibilidades que começam com "l"
# algo - > troca a primeira letra fixa
# alog - > ...
###############

r = []
def anagrama(letrasFixas, resto):
    if len(resto) <= 1: # quando chega no problema infantil, retorna a palavra inteira
        r.append(letrasFixas + resto)
        return letrasFixas + resto
    # elif len(resto) == 2: # se o tamanho da palavra for igual a 2, troca as letras restantes de lugar
    #     a, b = resto[1], resto[0]
    #     resto.replace(resto[0], a)
    #     resto.replace(resto[1], b)
    #     return resto
    else:
        for i in range(len(resto)):
            # adiciona mais uma letra nas letras fixas
            # e repete o processo com o resto da palavra
            anagrama(letrasFixas + resto[i], resto[:i] + resto[i+1:])

anagrama("","lago")
print(r)
