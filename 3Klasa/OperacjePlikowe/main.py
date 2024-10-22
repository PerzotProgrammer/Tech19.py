from random import randint
from zad5 import callAll as zad5
from zad6 import callAll as zad6


def zad1():
    with open("dane.txt", "w", encoding="UTF-8") as file:
        file.write(f"{input("Podaj imię: ")}\n")
        file.write(f"{input("Podaj nazwisko: ")}\n")
        file.close()


def zad2():
    with open("dane.txt", encoding="UTF-8") as file:
        print(f"Witaj {file.read().replace("\n", " ")}")
        file.close()


def zad3():
    with open("losowe.txt", "w") as file:
        for i in range(10):
            file.write(f"{randint(0, 100)}\n")
        file.close()
    with open("losowe.txt") as file:
        numbStr = file.read().split("\n")
        numbStr.pop()  # Usunięcie białego znaku na końcu
        numbers = []
        for num in numbStr:
            numbers.append(int(num))
        print(
            f"Suma liczb: {sum(numbers)}\nMaks: {max(numbers)}\nMin: {min(numbers)}\nŚrednia: {sum(numbers) / len(numbers)}")
        file.close()


def zad4():
    with open("ciagi.txt") as file:
        listOfEvens = []
        for line in file:
            listOfNumbs = []
            for num in line.split():
                listOfNumbs.append(int(num))
            if sum(listOfNumbs) % 2 == 0:
                listOfEvens.append(listOfNumbs)
        print(listOfEvens)
        file.close()


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
