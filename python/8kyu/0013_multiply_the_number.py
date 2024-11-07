#!/usr/bin/env python

from random import randint


# solution
def multiply(n):
    return n * (5 ** len(f"{abs(n)}"))


# test
for i in range(100):
    number = randint(-100, 100)
    print(multiply(number))

