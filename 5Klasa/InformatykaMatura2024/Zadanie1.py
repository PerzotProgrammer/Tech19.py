def obliczPlansze(A: list[list[bool]]) -> bool:
    n = len(A)
    m = len(A[0])
    P = [[False for _ in range(m)] for _ in range(n)]
    P[0][0] = True

    for i in range(n):
        for j in range(m):
            if not A[i][j]:
                P[i][j] = False
            elif i == 0 and j != 0:
                P[i][j] = P[i][j - 1]
            elif i != 0 and j == 0:
                P[i][j] = P[i - 1][j]
            elif i != 0 and j != 0:
                P[i][j] = P[i - 1][j] or P[i - 1][j]

    return P[n - 1][m - 1]


if __name__ == '__main__':
    print(obliczPlansze([[False, False, False],
                         [True, False, True],
                         [False, False, False]]))

    print(obliczPlansze([[False, False, False],
                         [True, True, False],
                         [False, False, False],
                         [False, True, True],
                         [False, False, False]]))

    print(obliczPlansze([[False, True, True, True, True],
                         [False, False, True, True, False],
                         [True, False, True, True, False],
                         [True, False, False, False, True],
                         [True, False, True, False, False]]))
