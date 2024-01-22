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


wykres1 = np.linspace(0, 30)

pp.plot(wykres1, f1(wykres1), color="blue")

pp.show()
