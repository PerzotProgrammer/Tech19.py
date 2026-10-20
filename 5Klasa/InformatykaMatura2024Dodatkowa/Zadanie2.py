def f(x: int) -> int:
    f.ileRekursji += 1
    if x == 0:
        return 0
    return 2 + f(x // 2)


f.ileRekursji = 0
if __name__ == '__main__':
    f.ileRekursji = 0
    print(f"{f(3)} {f.ileRekursji}")
    f.ileRekursji = 0
    print(f"{f(16)} {f.ileRekursji}")
    f.ileRekursji = 0
    print(f"{f(35)} {f.ileRekursji}")
