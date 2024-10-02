import BinarySearch as bs


def zad1():
    numbers = list(map(int, input("Podaj listę liczb: ").split()))
    if not bs.IsSorted(numbers):
        print("Lista musi być posortowana!")
        return
    searchedNumber = int(input("Podaj liczbę do znalezienia: "))
    indexOfNumber = bs.BinarySearch(numbers, searchedNumber)
    if indexOfNumber != -1:
        print(f"Liczba znajduje się w liście na indeksie {indexOfNumber}")
    else:
        print("Liczba nie znajduje się w liście")


if __name__ == "__main__":
    zad1()
