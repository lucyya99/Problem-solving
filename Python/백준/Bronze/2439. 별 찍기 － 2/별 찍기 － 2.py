import sys
N:int = int(sys.stdin.readline())
assert (N >= 1 and N <= 100)
assert type(N) == int

[print(' ' * (N - n - 1) + '*' * (n + 1)) for n in range(N)]