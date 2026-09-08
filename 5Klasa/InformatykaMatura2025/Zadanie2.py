def czy_palindrom(ciag: str) -> bool:
    for i in range(len(ciag) // 2):
        if ciag[i] != ciag[len(ciag) - 1 - i]:
            return False
    return True


def zad2_1(sciezka: str):
    with open(sciezka) as file:
        for line in file:
            ciag = str(line.strip())
            if czy_palindrom(ciag):
                print(ciag)


def zad2_2(sciezka: str):
    arr = []

    with open(sciezka) as file:
        for line in file:
            arr.append(line.strip())

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


def zad2_3(sciezka: str):
    liczba_max = 0
    nr_linii = 0
    arr = []

    with open(sciezka) as file:
        for line in file:
            arr.append(line.strip())

    for i in range(len(arr)):
        liczba_str = ""
        liczba = 0
        for j in range(len(arr[i])):
            if arr[i][j] == "o":
                liczba_str += "0"
            elif arr[i][j] == "+":
                liczba_str += "1"
            elif arr[i][j] == "*":
                liczba_str += "2"

        liczba = dziesietnie_z_systemu(liczba_str, 3)

        if liczba > liczba_max:
            liczba_max = liczba
            nr_linii = i

    print(f"{liczba_max} {arr[nr_linii]}")


if __name__ == '__main__':
    zad2_1("symbole_przyklad.txt")
    print("---------------------------")
    zad2_1("symbole.txt")
    print("---------------------------")
    zad2_2("symbole.txt")
    print("---------------------------")
    zad2_3("symbole_przyklad.txt")
    print("---------------------------")
    zad2_3("symbole.txt")
