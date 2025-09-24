def find_max_way_in_matrix(matrix: list[list[int]], report: bool = False) -> int:
    sum_of_vals = 0
    i = 0
    j = 0
    while i < len(matrix) - 1 or j < len(matrix[i]) - 1:
        if report:
            print(f"{i} {j}")
        if i == len(matrix) - 1:
            j = j + 1
        elif j == len(matrix[i]) - 1:
            i = i + 1
        elif matrix[i + 1][j] > matrix[i][j + 1]:
            i = i + 1
        else:
            j = j + 1
        sum_of_vals = sum_of_vals + matrix[i][j]
    return sum_of_vals
