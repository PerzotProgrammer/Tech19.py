def give_change(sum_of_money: int, denominations: list[int]) -> dict[int, int]:
    denominations.sort()
    denominations.reverse()
    change = {}
    for denomination in denominations:
        number_of_denomination = sum_of_money // denomination
        sum_of_money -= number_of_denomination * denomination
        change[denomination] = number_of_denomination

    return change
