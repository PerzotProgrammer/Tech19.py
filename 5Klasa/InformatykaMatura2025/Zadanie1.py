def przestaw(n: int) -> int:
    r: int = n % 100
    a: int = r // 10
    b: int = r % 10
    n: int = n // 100
    w: int
    if n > 0:
        w = int(a + 10 * b + 100 * przestaw(int(n)))
    else:
        if a > 0:
            w = int(a + 10 * b)
        else:
            w = b
    return w


if __name__ == '__main__':
    print(przestaw(316498))
    print(przestaw(43657688))
    print(przestaw(154005710))
    print(przestaw(998877665544321))
