import sys

H, x = map(int, sys.stdin.readline().split())
INF = 1000000007

snowball = 0
remember = 1
for i in range(H):
    remember *= x
    remember %= INF
    snowball += int(sys.stdin.readline())* remember
    snowball %= INF

print(snowball)