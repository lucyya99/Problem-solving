from sys import stdin
from collections import Counter

N, M = map(int, stdin.readline().split())
arr = Counter(map(int, stdin.readline().split()))

# 절단기에 설정할 수 있는 높이 = H => 나무의 최대 높이
start = 0
end = max(arr)

while start <= end:
    mid = start + (end - start) // 2
    # [T T T ... F F F]
    # sum > for (함수 콜링시 Pypi가 더 빠름 / Python3는 내장함수 사용해서 감싸는게 더 빠름)
    if sum((i - mid)*v for i, v in arr.items() if i - mid > 0) >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)