from factorization import IsPrime


def Ex1():
    with open("Numbers/liczby1.txt", "r") as f:
        lines = f.readlines()
        primes = []
        for line in lines:
            if IsPrime(int(line)):
                primes.append(int(line))
        print(f"W pliku jest {len(primes)} liczb pierwszych")


def Ex2():
    pass
