#!/usr/bin/env python3

def potInterativa(n, e):
    r = n
    for i in range(e-1):
        r *= n
    return r

def potRecursiva(n, e):
    if e == 0:
        return 1
    elif e <= 1:
        return n
    return n * potRecursiva(n, e-1)


print(potRecursiva(3,0))
print(potRecursiva(3,1))
print(potRecursiva(3,2))
print(potRecursiva(2,5))
print(potRecursiva(5,2))
