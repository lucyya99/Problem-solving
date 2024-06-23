# N = int(input())
# coordinates = []
# for n in range(N):
#     coordinates.append(list(map(int, input().split())))
# coordinates.sort()
#
# length = 0
# for i in range(N-1):
#     length += coordinates[i][1] - coordinates[i][0]
#     if coordinates[i][1] > coordinates[i+1][0]:
#         end = coordinates[i][1]
#         start = coordinates[i+1][0]
#         length -= end - start
#
# length += coordinates[-1][1] - coordinates[-1][0]
# print(length)

# N = int(input())
# coordinates = []
# for n in range(N):
#     coordinates.append(list(map(int, input().split())))
# coordinates.sort()
#
# length = 0
# for i in range(N-1):
#     length += coordinates[i][1] - coordinates[i][0]
#     if coordinates[i][1] > coordinates[i+1][0]:
#         end = coordinates[i][1]
#         start = coordinates[i+1][0]
#         length -= end - start
# length += coordinates[-1][1] - coordinates[-1][0]
# print(length)

import sys
N = int(sys.stdin.readline())
coordinates = []
for n in range(N):
    coordinates.append(list(map(int, sys.stdin.readline().split())))
coordinates.sort()

temp = 0
length = 0
left = -10000
right = -10000
for i in range(N):
    if coordinates[i][0] < right:
        right = max(right, coordinates[i][1])
    else:
        length += right - left
        left = coordinates[i][0]
        right = coordinates[i][1]
length += right - left
print(length)