def FastPower(base, exponent):
    output = 1
    while exponent > 0:
        if exponent % 2:
            output *= base
        base *= base
        exponent //= 2
    return output
