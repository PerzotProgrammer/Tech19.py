import SlidingWindow as sw


def zad1():
    sw.PrintAllSubarrayEx1(list(map(int, input("Podaj ciąg: ").split())))


def zad2():
    sw.PrintAllSubarrayEx2(list(map(int, input("Podaj ciąg: ").split())))


if __name__ == '__main__':
    zad1()
    zad2()
