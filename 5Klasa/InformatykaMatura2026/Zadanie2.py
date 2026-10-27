def liczPrzeniesienia(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        return 0

    p = 0
    aktMiejsce = 1
    pJed = 0
    while True:
        if aktMiejsce > a:
            return p
        aJed = (a // aktMiejsce) % 10
        bJed = (b // aktMiejsce) % 10
        if aJed + bJed + pJed >= 10:
            p += 1
            pJed = 1
        else:
            pJed = 0
        aktMiejsce *= 10


if __name__ == '__main__':
    print(liczPrzeniesienia(27732, 72619))
