from typing import Any

N, find = [int(input()) for _ in range(2)]

# init
x_pos, y_pos = N//2, N//2   # 시작: 중간
N_2 = N * N                 # end
move_dir = 0
move = 1
move_power = 1
num = 1
arr = [[0 for _ in range(N)] for _ in range(N)]
target_x_pos, target_y_pos = 0, 0

for _ in range(N_2):
    arr[y_pos][x_pos] = str(num)

    if num == find:
        target_x_pos, target_y_pos = y_pos+1, x_pos+1

    if move <= 0:
        move = move_power
        # 방향 변경
        move_dir = (move_dir + 1) % 4
        # 얼마나 움직일지도 변경
        if move_dir == 0 or move_dir == 2:
            move_power += 1
            move += 1

    # dir -> 4개 = 0, 1, 2, 3
    if move_dir == 0:  # up
        y_pos -= 1
    elif move_dir == 1:  # right
        x_pos += 1
    elif move_dir == 2:  # down
        y_pos += 1
    elif move_dir == 3:  # left
        x_pos -= 1

    move -= 1
    num += 1


for row in arr:
    print(" ".join(row))
print(target_x_pos, target_y_pos)