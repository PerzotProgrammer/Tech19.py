def PrintAllSubarrayEx1(T: list[int]) -> None:
    i = 0
    size = 1
    j = size
    while j <= len(T):
        while j <= len(T):
            print(T[i:j])
            i += 1
            j += 1
        i = 0
        size += 1
        j = size


def PrintAllSubarrayEx2(T: list[int]) -> None:
    for i in range(len(T)):
        for j in range(i + 1, len(T) + 1):
            print(T[i:j])
