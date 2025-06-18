with open("./dane2_3.txt", "r") as file:
    for line in file:
        line = line.strip()
        depth = 0
        max_depth = 0
        for char in line:
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
            if depth > max_depth:
                max_depth = depth
        print(max_depth)