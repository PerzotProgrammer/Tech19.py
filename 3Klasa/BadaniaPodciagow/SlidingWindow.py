def GetAllSubarrays(T: list[int], lengthLimit: int = -1) -> list[list[int]]:
    Subarrays = []
    if lengthLimit < 0:
        for i in range(len(T)):
            for j in range(i + 1, len(T) + 1):
                Subarrays.append(T[i:j])
    else:
        for i in range(0, len(T) - lengthLimit + 1):
            j = i + lengthLimit
            Subarrays.append(T[i:j])
    return Subarrays
