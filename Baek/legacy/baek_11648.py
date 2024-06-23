import sys


def divide_10(N):
    mul = 1
    while N >= 10:
        mul *= (N % 10)
        N //= 10
    mul *= N
    return mul


N = int(input())
mul = N
cnt = 0
while mul >= 10:
    mul = divide_10(N)
    cnt += 1
    N = mul

print(cnt)