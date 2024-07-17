N, M = map(int, input().split())
arr = [int(n) for n in input().split()]
# 절단기에 설정할 수 있는 높이 = H => 나무의 최대 높이
start = 0
end = max(arr)

while start <= end:
    mid = start + (end - start) // 2
    # [T T T ... F F F]
    H = sum(n - mid for n in arr if n - mid > 0)
    if H >= M:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)