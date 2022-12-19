#!/usr/bin/env python3

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    b = fibonacci(n-1)
    a = fibonacci(n-2)
    return a + b

for i in range(10):
    print(fibonacci(i))
