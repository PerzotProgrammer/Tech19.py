from MatrixExplorer import find_max_way_in_matrix


def zad4():
    matrix = []
    with open("macierz.txt") as file:
        for line in file.readlines():
            matrix.append(list(map(int, line.split())))

    print(matrix)
    print(find_max_way_in_matrix(matrix, True))


if __name__ == '__main__':
    zad4()
