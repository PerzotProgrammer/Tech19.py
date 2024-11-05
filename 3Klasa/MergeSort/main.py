from random import randint
import MergeSort


def zad1():
    T = list(map(int, input("Podaj ciąg oddzielony spacjami: ").split()))
    print(f"Tablica po posortowaniu: {MergeSort.Sort(T)}")


def zad2():
    T = []
    with open("ciagi.txt") as file:
        for line in file:
            T.extend(list(map(int, line.split())))
    T = MergeSort.Sort(T)
    with open("wyniki_2.txt", "w") as file:
        file.write(" ".join(map(str, T)))


def zad3():
    T = [randint(1, 1_000_000) for _ in range(1_000_000)]
    MergeSort.Sort(T)
    with open("wyniki_3.txt", "w") as file:
        file.write("\n".join(map(str, T)))


if __name__ == "__main__":
    zad1()
    zad2()
    zad3()
