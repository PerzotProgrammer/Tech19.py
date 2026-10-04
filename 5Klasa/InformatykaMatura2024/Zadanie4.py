def wczytajPlik(plik: str) -> tuple[list[int], list[int]]:
    macierz = []
    with open(plik) as file:
        for line in file:
            macierz.append(list(map(int, line.split())))

    return macierz[0], macierz[1]


def zad4_1(plik: str):
    dzielniki, liczby = wczytajPlik(plik)

    ileDzielnikow = 0

    for i in range(len(dzielniki)):
        for j in range(len(liczby)):
            if liczby[j] % dzielniki[i] == 0:
                ileDzielnikow = ileDzielnikow + 1
                break

    print(ileDzielnikow)


def zad4_2(plik: str):
    liczby, _ = wczytajPlik(plik)

    for i in range(1, len(liczby)):
        for j in range(1, len(liczby)):
            if liczby[j - 1] < liczby[j]:
                liczby[j - 1], liczby[j] = liczby[j], liczby[j - 1]

    print(liczby[102])


def naIloczynyPierwsze(n: int) -> list[int]:
    arr = []

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                arr.append(i)
                break
    return arr


def zawiera(lista: list[int], zawartosc: list[int]) -> bool:
    listaKopia = lista.copy()

    for n in zawartosc:
        if n not in listaKopia:
            return False
        listaKopia.remove(n)
    return True


def zad4_3(plik: str):
    iloczyny, liczby = wczytajPlik(plik)

    znalezione = []

    for n in liczby:
        ilPierwsze = naIloczynyPierwsze(n)
        if zawiera(iloczyny, ilPierwsze):
            znalezione.append(n)

    print(znalezione)


def zad4_4(plik: str):
    liczby, _ = wczytajPlik(plik)

    najlepszyPoczatek = 0
    najlepszaSuma = sum(liczby[:50])
    najlepszaDlugosc = 50

    for poczatek in range(len(liczby)):
        for koniec in range(poczatek + 50, len(liczby) + 1):
            suma = sum(liczby[poczatek:koniec])
            dlugosc = koniec - poczatek

            if suma * najlepszaDlugosc > najlepszaSuma * dlugosc:
                najlepszyPoczatek = poczatek
                najlepszaSuma = suma
                najlepszaDlugosc = dlugosc

    najwyzszaSrednia = najlepszaSuma / najlepszaDlugosc
    print(
        round(najwyzszaSrednia, 2),
        najlepszaDlugosc,
        liczby[najlepszyPoczatek],
    )


if __name__ == '__main__':
    print("zad 4.1 p")
    zad4_1("liczby_przyklad.txt")
    print("zad 4.1")
    zad4_1("liczby.txt")

    print("zad 4.2 p")
    zad4_2("liczby_przyklad.txt")
    print("zad 4.2")
    zad4_2("liczby.txt")

    print("zad 4.3 p")
    zad4_3("liczby_przyklad.txt")
    print("zad 4.3")
    zad4_3("liczby.txt")

    print("zad 4.4 p")
    zad4_4("liczby_przyklad.txt")
    print("zad 4.4")
    zad4_4("liczby.txt")
