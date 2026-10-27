class Rekurencja:

    def __init__(self):
        self.licznikReku = 0

    def A(self, m: int, n: int) -> int:
        self.licznikReku += 1
        print(f"A({m},{n})")
        if n > 1:
            if n % 2 == 0:
                return self.A(2 * m, n // 2)
            elif n % 2 != 0:
                return 2 * self.A(m, (n - 1) // 2) + m
        return m

    def sprawdzReku(self, m: int, n: int):
        print(f"{self.A(m, n)} liczba wywołań: {self.licznikReku}")
        self.licznikReku = 0


if __name__ == '__main__':
    reku = Rekurencja()

    reku.sprawdzReku(3, 9)
    reku.sprawdzReku(pow(2, 5), pow(2, 5))
    reku.sprawdzReku(10, 15)
    reku.sprawdzReku(1, pow(2, 100) + 1)

    reku.sprawdzReku(1, 777)
    reku.sprawdzReku(2 * pow(10, 6), 256 * pow(10, 6))
