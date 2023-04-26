# DZIAŁANIE
# wejście = "ABCCCDDDDDEFGGGHHIJJ"
# wyjście = "AB3C5DEF3G2HI2J"

msg = input("Podaj ciąg: ")

out = ""
ilosc = 1
for i in range(len(msg) - 1):
    if msg[i] == msg[i + 1]:
        ilosc += 1
    else:
        if ilosc > 1:
            out += str(ilosc)
            ilosc = 1
        out += msg[i]
if ilosc > 1:
    out += str(ilosc)
out += msg[len(msg) - 1]

print("Wynik:", out)