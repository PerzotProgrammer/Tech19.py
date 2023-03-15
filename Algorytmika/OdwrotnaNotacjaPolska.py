# Optymalizacja zapisu nie była moim celem

ciag = input("Podaj ciąg lolu: ")
stos = []

for num in ciag:
    if num.isdigit():
        stos.append(num)
    else:
        if num == "+":
            wynik = int(stos[len(stos)-2]) + int(stos[len(stos)-1])
            stos.pop()
            stos.pop()
            stos.append(wynik)
        if num == "-":
            wynik = int(stos[len(stos)-2]) - int(stos[len(stos)-1])
            stos.pop()
            stos.pop()
            stos.append(wynik)
        if num == "*":
            wynik = int(stos[len(stos)-2]) * int(stos[len(stos)-1])
            stos.pop()
            stos.pop()
            stos.append(wynik)
        if num == "/":
            wynik = int(stos[len(stos)-2]) // int(stos[len(stos)-1])
            stos.pop()
            stos.pop()
            stos.append(wynik)

print("Twój wynik lolu:",stos[0])