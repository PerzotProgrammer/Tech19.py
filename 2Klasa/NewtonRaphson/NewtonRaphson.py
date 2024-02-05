def NewtonRaphson(p, n):
    a = p
    b = 1
    for i in range(n):
        a = (a + b) / 2
        b = p / a
    return a
