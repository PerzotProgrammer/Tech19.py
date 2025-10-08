from ChangeAlgorithm import give_change


def zad1():
    with open("dane.txt") as file:
        denominations = list(map(int, file.readline().split()))
        values = list(map(int, file.readlines()))

    min_sum_of_money = float('inf')
    mins_of_values = []

    for value in values:
        change = give_change(value, denominations)
        sum_of_money = 0
        for denomination in denominations:
            sum_of_money += change[denomination]

        if sum_of_money < min_sum_of_money:
            mins_of_values.clear()
            min_sum_of_money = sum_of_money
        if min_sum_of_money == sum_of_money:
            mins_of_values.append(value)

    print(mins_of_values)


if __name__ == '__main__':
    zad1()
