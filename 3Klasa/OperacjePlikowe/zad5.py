def a():
    with open('slowa.txt', 'r') as file:
        lineNumber = 1
        for line in file:
            print(f"Linia {lineNumber}: {line.strip("\n")}")
            lineNumber += 1
        file.close()


def b():
    with open('slowa.txt', 'r') as file:
        lineNumber = len(file.read().strip().split("\n"))
        print(f"Ilość linii: {lineNumber}")
        file.close()


def c():
    with open('slowa.txt', 'r') as file:
        lines = file.read().split("\n")
        lines.pop()
        for line in lines:
            if line[0] == "A":
                print(line)
        file.close()


def d():
    with open('slowa.txt', 'r') as file:
        lines = file.read().split("\n")
        lines.pop()
        for line in lines:
            if line[len(line) - 1] == "A":
                print(line)
        file.close()


def e():
    with open('slowa.txt', 'r') as file:
        lines = file.read().split("\n")
        lines.pop()
        for line in lines:
            numOfLetters = len(line)
            print(f"{line} - {numOfLetters}")
        file.close()


def f():
    with open('slowa.txt', 'r') as file:
        minLen = 10000000000
        maxLen = 0
        minLenWord = ""
        maxLenWord = ""
        lines = file.read().split("\n")
        lines.pop()
        for line in lines:
            if len(line) < minLen:
                minLen = len(line)
                minLenWord = line
            elif len(line) > maxLen:
                maxLen = len(line)
                maxLenWord = line
        print(f"Najkrótsze słowo: {minLenWord}")
        print(f"Najdłuższe słowo: {maxLenWord}")


def callAll():
    a()
    b()
    c()
    d()
    e()
    f()


if __name__ == "__main__":
    callAll()
