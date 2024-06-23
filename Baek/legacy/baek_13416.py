daily_max = 0
total_max = 0
T = int(input())    # Testcase
for t in range(T):  # 2
    N = int(input())  # 주식 일 수 4
    for n in range(N):
        day_list = list(map(int, input().split()))
        if day_list[0] < 0 and day_list[1] < 0 and day_list[2] < 0:
            continue
        daily_max = max(day_list)
        daily_max = max(daily_max, 0)
        total_max += daily_max
    print(total_max)
    total_max = 0
