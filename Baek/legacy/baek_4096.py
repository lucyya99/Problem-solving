import sys


def is_same_str(arr):
    n_half = len(arr) // 2
    cnt = 0
    for idx in range(n_half):
        if arr[idx] == arr[-1 - idx]:
            cnt += 1
    if cnt == n_half:
        return True
    else:
        return False


def add_zero(number, n):
    zero = ""
    for _ in range(len(str(number)), n):
        zero += '0'
    return zero + str(number)


lines = []
while True:
    data = sys.stdin.readline().rstrip()
    if data == '0':
        break
    lines.append(data)
for line in lines:
    N = len(line)
    pace = 0
    while not is_same_str(line):
        pace += 1
        num = int(line) + 1
        line = add_zero(num, N)
    print(pace)
