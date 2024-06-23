import sys
N = int(sys.stdin.readline())
square_info = []
z_buffer = [[-1]*1001 for j in range(1001)]
area = [0 for n in range(N)]
for n in range(N):
    square_info.append(list(map(int, sys.stdin.readline().split())))

# 끝점 계산
for square in square_info:
    square[2] = square[0]+square[2]
    square[3] = square[1]+square[3]

# 실제 좌표에 나타날 index 저장
for i, square in enumerate(square_info):
    # end point
    x1 = square[0]
    y1 = square[1]
    x2 = square[2]
    y2 = square[3]
    for x in range(x1, x2):
        for y in range(y1, y2):
            z_buffer[x][y] = i

# sum of area
for i, square in enumerate(square_info):
    # end point
    x1 = square[0]
    y1 = square[1]
    x2 = square[2]
    y2 = square[3]
    for x in range(x1, x2):
        for y in range(y1, y2):
            if z_buffer[x][y] == i:
                area[i] += 1
    print(area[i])