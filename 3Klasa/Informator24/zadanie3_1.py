with open("./dane3.txt", "r") as file:
    smallest = 5_000
    secondSmallest = 5_000
    for line in file:
        num1, num2 = list(map(int, line.strip().split()))
        length = num2 - num1 + 1
        if length < smallest:
            secondSmallest = smallest
            smallest = length
    print(secondSmallest, smallest)