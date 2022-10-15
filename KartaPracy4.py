#TODO zad1

#zad2
from math import floor


def dodaj(x,y):
    return x+y

#zad3
def silnia(x):
    if x == 0 : return 1
    else : return x * silnia(x-1)

#zad4
def fib(x):
    if x == 1 or x == 2 : return 1
    else : return fib(x-1) + fib(x-2)

#TODO zad5

#zad6
def po(x,y):
    if y == 0 : return 1
    if y == 1 : return x
    else : return x * po(x,y-1)

#zad7
def binar(x):
    if x == 1 : return 1
    else : 
        num = x
        i = x % 2
        x = floor(x/2)
        print(num,i)
        return binar(x)


#TODO wyniki