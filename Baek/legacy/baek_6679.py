def calc_decimal(N: int, decimal: int) -> int:
    sum = 0
    while N > 0:
        sum += (N % decimal)
        N = N // decimal
    return sum


for i in range(1000, 10000):
    decimal_10 = calc_decimal(i, 10)
    decimal_12 = calc_decimal(i, 12)
    decimal_16 = calc_decimal(i, 16)
    if decimal_10 == decimal_12 and decimal_12 == decimal_16:
        print(i)