napis = input("Podaj napis do szyfracji: ")
szyfr = ""
przelorzenie = 3

for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + przelorzenie) % 26)
print("Szyfracja:", szyfr)

szyfr = ""

for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 - przelorzenie) % 26)
print("Deszyfracja:", szyfr)
