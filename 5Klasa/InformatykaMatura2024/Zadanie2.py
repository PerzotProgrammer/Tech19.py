def algorytmCyfr(n: int):
    b = 1
    c = 0

    ileC = 0

    while n > 0:
        a = n % 10
        n = n // 10
        if a % 2 == 0:
            c = c + b * (a // 2)
        else:
            c = c + b
            ileC += 1
        b = b * 10

    print(f"Wartość c {c}, liczba instrukcji {ileC}")


if __name__ == '__main__':
    algorytmCyfr(33658)
    algorytmCyfr(542102)
    algorytmCyfr(87654321012345678)

    algorytmCyfr(333333666666999999)
