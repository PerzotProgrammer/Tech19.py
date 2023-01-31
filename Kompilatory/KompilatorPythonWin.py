# Moja autorska wersja kompilatora pod Pythona
# Wykorzystuje ona wbudowane biblioteki (przynajmniej na Windowsie)


import py_compile, os

path = str(input("Podaj ścieżkę do kompilacji: "))
path = os.path.dirname(__file__) + "/" + path

if os.path.isfile(path):

    if path.endswith(".py"):
        py_compile.compile(path)
        print("Znaleziono plik!\nSprawdź folder __pycache__ (plik powinien nazywać się nazwaPliku-cpython-wersja.pyc)")
        input("naciśnij klawisz aby zamknąć program...").split()

    else:
        print("Niepoprawnie rozszerzenie pliku!\nUpewnij się, że plik kończy się na .py")


elif os.path.isdir(path):
    print("Podano folder a nie plik!\nPliki w folderze:\n",os.listdir(path))
    input("naciśnij klawisz aby zamknąć program...").split()

else:
    print("Nie można znaleść scieżki\nUpewnij się, że scieżka jest relatywna względęm położenia tego pliku!")
    input("naciśnij klawisz aby zamknąć program...").split()
