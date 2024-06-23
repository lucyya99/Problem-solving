import sys


def factorization(num):
    factor = 2
    while num != 1:
        if num % factor == 0:
            print(factor)
            factorization(num // factor)
            return
        factor += 1


N = int(sys.stdin.readline())
factorization(N)

# import sys
#
# v = int(sys.stdin.readline())
# i = 2
# while v != 1:
#     if v % i == 0:
#         v /= i
#         print(i)
#     else:
#         i += 1
