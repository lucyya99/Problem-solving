import sys

N: int = int(sys.stdin.readline())
sqrt: int = 100
tolerance = 0.1
diff: int = 1
while diff >= tolerance:
    before = sqrt
    sqrt = (sqrt + N // sqrt) // 2
    diff = abs(before - sqrt)
print(int(sqrt))

# import sys
#
# N = int(sys.stdin.readline())
# sys.setrecursionlimit(10 ** 6)
#
#
# def sqrt(s, e):
#     if s > e:
#         return e
#     mid = (s + e) // 2
#     mid_2 = mid * mid
#     if mid_2 == N:
#         return mid
#     elif mid_2 > N:
#         return sqrt(s, mid - 1)
#     else:
#         return sqrt(mid + 1, e)
#
#
# print(sqrt(1, N))
