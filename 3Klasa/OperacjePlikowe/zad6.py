def a():
    with open("liczby.txt", "r") as file:
        print(f"W pliku jest {len(file.readlines())} liczb")
        file.close()


def b():
    with open("liczby.txt", "r") as file:
        for line in file:
            if line.strip()[-1] == "0":
                print(f"{line.strip()}")
        file.close()


def c():
    with open("liczby.txt", "r") as file:
        for line in file:
            if line.strip()[-1] == "0" and line.strip()[-2] == "0" and line.strip()[-3] == "0":
                print(f"{line.strip()}")
        file.close()


def d():
    with open("liczby.txt", "r") as file:
        for line in file:
            if line.strip().count("0") < line.strip().count("1"):
                print(f"{line.strip()}")
        file.close()


def e():
    with open("liczby.txt", "r") as file:
        for line in file:
            print(int(line, 2))


def callAll():
    a()
    b()
    c()
    d()
    e()


if __name__ == "__main__":
    callAll()
