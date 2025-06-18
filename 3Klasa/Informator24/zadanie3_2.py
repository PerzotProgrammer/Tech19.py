with open("./dane3.txt", "r") as file:
    count_of_lengths = [0] * 5_000
    max_length = 0
    size_of_interval = 0
    for line in file:
        num1, num2 = list(map(int, line.strip().split()))
        length = num2 - num1 + 1
        count_of_lengths[length] += 1
    for i in range(len(count_of_lengths)):
        if count_of_lengths[i] > max_length:
            size_of_interval = i
            max_length = count_of_lengths[i]
    print(size_of_interval, max_length)
