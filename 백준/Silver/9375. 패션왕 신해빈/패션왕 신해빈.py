from sys import stdin
from collections import Counter

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    clothes = []
    for __ in range(n):
        cloth, cate = stdin.readline().split()
        clothes.append(cate)

    clothes = Counter(clothes)

    cnt = 1
    for key in clothes:
        cnt *= clothes[key] + 1

    print(cnt - 1)