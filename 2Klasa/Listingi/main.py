def f1(x):
    return -x ** 2 + 6 * x + 2


def prostokaty1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f1(a + i * dx) * dx
    return s


def prostokaty2(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f1(a + dx / 2 + i * dx) * dx
    return s


def prostokaty3(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f1(a + dx + i * dx) * dx
    return s


def trapezy1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += (f1(a + i * dx) + f1(a + (i + 1) * dx)) * dx / 2
    return s


def trapezy2(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += 2 * f1(a + i * dx)
    return s * dx / 2
