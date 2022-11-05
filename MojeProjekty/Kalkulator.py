#KALKULATOR
liczba1 = float(input("Podaj liczbę: "))
i = 0
while True:

    znak = str(input("Podaj znak: "))

    if znak == "+":
        liczba2 = float(input("Podaj liczbę: "))
        liczba1 += liczba2
        i = 1

    elif znak == "-":
        liczba2 = float(input("Podaj liczbę: "))
        liczba1 -= liczba2
        i = 1
    
    elif znak == "*":
        liczba2 = float(input("Podaj liczbę: "))
        liczba1 *= liczba2
        i = 1
    
    elif znak == "/":
        liczba2 = float(input("Podaj liczbę: "))
       
        if liczba1 == 0 or liczba2 == 0:
            print("NIE MOŻNA DZIELIĆ PRZEZ 0!")
            i = 0
        
        else:
            liczba1 /= liczba2
            i = 1
    
    elif znak == "**":
        liczba2 = float(input("Podaj liczbę: "))
        liczba1 **= liczba2
        i = 1

    else:
        print("ZŁY ZNAK!")
        i = 0

    if i == 1:
        print(f"Wynik: {liczba1}")
    
    print("-----------")