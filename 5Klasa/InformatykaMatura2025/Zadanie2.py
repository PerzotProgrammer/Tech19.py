def zwroc_plik(sciezka: str) -> list[str]:
    arr = []

    with open(sciezka) as file:
        for line in file:
            arr.append(line.strip())
    return arr


def czy_palindrom(ciag: str) -> bool:
    for i in range(len(ciag) // 2):
        if ciag[i] != ciag[len(ciag) - 1 - i]:
            return False
    return True


def zad2_1(sciezka: str):
    arr = zwroc_plik(sciezka)
    for ciag in arr:
        if czy_palindrom(ciag):
            print(ciag)


def zad2_2(sciezka: str):
    arr = zwroc_plik(sciezka)

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):

            if (
                    arr[i - 1][j - 1] == arr[i - 1][j] == arr[i - 1][j + 1]
                    and arr[i][j - 1] == arr[i][j] == arr[i][j + 1]
                    and arr[i + 1][j - 1] == arr[i + 1][j] == arr[i + 1][j + 1]
                    and arr[i - 1][j] == arr[i][j] == arr[i + 1][j]
            ):
                print(f"{i + 1} - {j + 1}")


def dziesietnie_z_systemu(liczba_str: str, system: int) -> int:
    liczba = 0
    for i in range(len(liczba_str)):
        liczba = liczba * system + int(liczba_str[i])
    return liczba


def z_dziesietnych_na_system(liczba: int, system: int) -> str:
    if liczba == 0:
        return "0"

    liczba_str = ""

    while liczba > 0:
        reszta = liczba % system
        liczba_str += str(reszta)
        liczba //= system

    return odwroc_ciag(liczba_str)


def odwroc_ciag(ciag: str) -> str:
    arr = list(ciag)

    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return "".join(arr)


def liczba_trojkowa(liczba_str: str, czy_ze_znakowej: bool = True) -> str:
    wyjscie = ""
    if czy_ze_znakowej:
        for znak in liczba_str:
            if znak == "o":
                wyjscie += "0"
            elif znak == "+":
                wyjscie += "1"
            elif znak == "*":
                wyjscie += "2"
    else:
        for znak in liczba_str:
            if znak == "0":
                wyjscie += "o"
            elif znak == "1":
                wyjscie += "+"
            elif znak == "2":
                wyjscie += "*"
    return wyjscie


def zad2_3(sciezka: str):
    liczba_max = 0
    nr_linii = 0
    arr = zwroc_plik(sciezka)

    for i in range(len(arr)):
        liczba = dziesietnie_z_systemu(liczba_trojkowa(arr[i]), 3)

        if liczba > liczba_max:
            liczba_max = liczba
            nr_linii = i

    print(f"{liczba_max} {arr[nr_linii]}")


def zad2_4(sciezka: str):
    suma = 0

    arr = zwroc_plik(sciezka)

    for ciag in arr:
        suma += dziesietnie_z_systemu(liczba_trojkowa(ciag), 3)

    print(f"{suma} {liczba_trojkowa(z_dziesietnych_na_system(suma, 3), False)}")


if __name__ == '__main__':
    print("Zadanie 2.1 p")
    zad2_1("symbole_przyklad.txt")

    print("Zadanie 2.1")
    zad2_1("symbole.txt")

    print("Zadanie 2.2 p")
    zad2_2("symbole_przyklad.txt")

    print("Zadanie 2.2")
    zad2_2("symbole.txt")

    print("Zadanie 2.3 p")
    zad2_3("symbole_przyklad.txt")

    print("Zadanie 2.3")
    zad2_3("symbole.txt")

    print("Zadanie 2.4 p")
    zad2_4("symbole_przyklad.txt")

    print("Zadanie 2.4")
    zad2_4("symbole.txt")
