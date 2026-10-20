def zadanie1(w: int, k: int, n: int) -> int:
    dlugosc = 0
    temp = n
    while temp > 0:
        dlugosc += 1
        temp //= 2

    ileKomorek = w * k
    lewa = ileKomorek % dlugosc

    if lewa == 0:
        lewa = dlugosc

    prawa = dlugosc - lewa

    for i in range(prawa):
        n = n // 2

    return n % 2


if __name__ == '__main__':
    print(zadanie1(5, 3, 19))
    print(zadanie1(4, 5, 179))
