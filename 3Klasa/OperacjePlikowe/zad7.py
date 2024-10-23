from random import randint


def a():
    with open("losowe_w_linii.txt", "w") as file:
        buff = ""
        for i in range(20):
            buff += f"{randint(1, 10)} "
        file.write(f"{buff}\n")


def b():
    with open("losowe_w_linii.txt") as file:
        nums = file.read().strip().split(" ")
        counts = [0 for i in range(11)]
        for num in nums:
            counts[int(num)] += 1
        maxCount = max(counts)
        maxCountNums = []
        for num in nums:
            if counts[int(num)] == maxCount and num not in maxCountNums:
                maxCountNums.append(num)
        print(f"W pliku najczęściej występują: {maxCountNums}, ich wystąpienia to {maxCount} razy")


def callAll():
    a()
    b()


if __name__ == "__main__":
    callAll()
