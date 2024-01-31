from random import randint


def MakeGraph(nodes: int, joints: int) -> {}:
    D = {}
    for i in range(nodes):
        D[i] = []

    for i in range(joints):
        # p, q = map(int, input().split())
        p = randint(0, 9)
        q = randint(0, 9)
        D[p].append(q)
        D[q].append(p)
    return D


# Stumilowy las

def StumilowyLas():
    a = 5
    b = 3
    D = {}
    for i in range(a):
        D[i + 1] = []

    for i in range(b):
        p, q = map(int, input().split())
        D[p].append(q)
        D[q].append(p)

    for i in range(1, a + 1):
        if len(D[i]) == 0:
            print("WIEWIÓR SAM")
        else:
            D[i].sort()
            for j in range(len(D[i])):
                print(D[i][j], end=" ")
            print()
    print()
