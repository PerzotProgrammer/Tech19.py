import matplotlib.pyplot as pp
import numpy as np


def f1(x):
    return np.sqrt(x)


def f2(a, b, n):
    h = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f1(a + i * h + h / 2) * h
    return suma


def f3(x):
    return 3 + 2 * x - np.power(x, 2)


wykres = np.linspace(0, 30)

pp.plot(wykres, f1(wykres), color="blue")
pp.plot(wykres, f2(wykres, 10, 10), color="green")
pp.plot(wykres, f3(wykres), color="red")

pp.show()
