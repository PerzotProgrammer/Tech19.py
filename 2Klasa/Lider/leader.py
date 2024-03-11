def Leader(T: list[int]) -> int | None:
    candidate = T[0]
    freq = 1
    for i in range(1, len(T)):
        if freq == 0:
            candidate = T[i]
            freq = 1
        else:
            if T[i] == candidate:
                freq += 1
            else:
                freq -= 1
    if freq == 0:
        return None
    else:
        numOfCandidates = 0
        for i in range(1, len(T)):
            if T[i] == candidate:
                numOfCandidates += 1
    if numOfCandidates > len(T) / 2:
        return candidate
