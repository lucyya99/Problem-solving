import sys
arr = list(map(int, sys.stdin.readline().split()))
N = arr[-1]
arr = arr[:-1]
escape = False
if 1 in arr:
    print(1)
    escape = True
arr.sort(reverse=True)
num = []
for i in range(0, N//arr[1]+1):
    num.append(i * arr[1])

for i in range(0, N//arr[0]+1):
    if escape:
        break
    if N == 0:
        print(1)
        escape = True
        break
    for n in num:
        buf = N-n
        if buf == 0:
            print(1)
            escape = True
            break
        elif buf < 0:
            break

        if buf % arr[2] == 0:
            print(1)
            escape = True
            break
    N -= arr[0]

if not escape:
    print(0)
