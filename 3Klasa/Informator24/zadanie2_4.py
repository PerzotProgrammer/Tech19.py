with open("./dane2_4.txt", "r") as file:
    for line in file:
        line = line.strip()
        balance = 0
        for char in line:
            if char == "[":
                balance += 1
            elif char == "]":
                balance -= 1
                if balance < 0:
                    break
        print("Tak" if balance == 0 else "Nie")
