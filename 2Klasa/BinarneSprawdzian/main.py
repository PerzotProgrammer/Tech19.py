# Pre
import math


def BinToDecimal(num: str) -> int:
    output = 0
    power = 0
    negative = False
    for i in range(len(num) - 1, -1, -1):
        if num[i] == "1":
            output += 2 ** power
        power += 1
        if num[i] == "-":
            negative = True
    if negative:
        return -output
    return output


def BubbleSort(T: list[str]) -> None:
    for i in range(0, len(T) - 1):
        for j in range(i, len(T)):
            if BinToDecimal(T[j]) > BinToDecimal(T[i]):
                T[j], T[i] = T[i], T[j]


# bez pliku .txt, ponieważ nie chcę mieć 1k dodanych linijek zwykłych danych
with open("./.venv/dane_systemy1.txt") as file:
    T = file.read().split("\n")

Times = []
Temps = []

for i in T:
    space = False
    time = ""
    temp = ""
    for j in i:
        if j == " ":
            space = True
        if space:
            temp += j
        else:
            time += j
    Times.append(time)
    Temps.append(temp)

# ZADANIE 1

TempsCopy = Temps.copy()
BubbleSort(TempsCopy)
print(f"Najniższa temperetura to {TempsCopy[len(TempsCopy) - 1]}")
print(f"Najwyższa temperetura to {TempsCopy[0]}")

# ZADANIE 2

numOfErrors = 0
for i in range(1, len(Times)):
    if BinToDecimal(Times[i - 1]) != BinToDecimal(Times[i]) - 24:
        numOfErrors += 1

print(f"Jest {numOfErrors} źle zmierzonych pomiarów")

# ZADANIE 3

bestDays = 0
lastBest = BinToDecimal(Temps[0])
for i in range(1, len(Temps)):
    if lastBest < BinToDecimal(Temps[i]):
        bestDays += 1
        lastBest = BinToDecimal(Temps[i])

print(f"Jest {bestDays} nowych najcieplejszych dni")

# ZADANIE 4

T = Temps.copy()
bestJump = 0

for i in range(0, len(T) - 1):
    for j in range(i + 1, len(T)):
        r = (BinToDecimal(T[i]) - BinToDecimal(T[j])) ** 2
        diff = i - j if i > j else j - i
        # Tak nie można, ale tak działa
        div = math.ceil(r / diff)
        if div > bestJump:
            bestJump = div

print(f"Największy skok temperatury to {bestJump}")
