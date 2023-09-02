string = input("Podaj stringa: ")
L = list(string)
R = L.copy()

R.reverse()

if R == L:
    print("JEST TO PALINDROM")
else :
    print("NIE JEST TO PALINDROM")
