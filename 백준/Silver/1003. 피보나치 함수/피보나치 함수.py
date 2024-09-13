from sys import stdin

fibo = [-1] * 41
fibo[0] = 0
fibo[1] = 1

fibo_0 = [0] * 41
fibo_0[0] = 1
fibo_1 = [0] * 41
fibo_1[1] = 1


def fibonacci(n: int) -> int:
    global fibo, fibo_0, fibo_1
    if fibo[n] < 0:
        fibo[n] = fibonacci(n-1) + fibonacci(n - 2)
        fibo_0[n] = fibo_0[n-2] + fibo_0[n-1]
        fibo_1[n] = fibo_1[n-2] + fibo_1[n-1]
    return fibo[n]


fibonacci(40)

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    print(fibo_0[N], fibo_1[N])