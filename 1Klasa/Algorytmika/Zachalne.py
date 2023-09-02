# Program sprawdzający nominały w podanej kwocie

kwota = int(input())
Nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
OutNominal = []

while kwota > 0:
    for nominal in Nominaly:
        ile = kwota // nominal
        kwota -= nominal * ile
        if ile > 0:
            for i in range(ile):
                OutNominal.append(nominal)
            print(f"nominał {nominal} występuje {ile} razy")
 
print(f"\nW sumie twoje nominały: {OutNominal}")
