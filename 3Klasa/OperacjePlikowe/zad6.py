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


def callAll():
    a()
    b()


if __name__ == "__main__":
    callAll()
