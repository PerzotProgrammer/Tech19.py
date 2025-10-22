def give_change_memo(sum_of_money: int, denominations: list[int]) -> int:
    denominations.sort()
    denominations.reverse()
    memo = [sum_of_money + 1 for _ in range(sum_of_money + 1)]

    memo[0] = 0

    for i in range(1, sum_of_money + 1):
        for j in range(len(denominations)):
            denomination = denominations[j]
            if i >= denomination:
                if memo[i - denomination] + 1 < memo[i]:
                    memo[i] = memo[i - denomination] + 1
    if memo[sum_of_money] != sum_of_money + 1:
        return memo[sum_of_money]
    return -1