# T = int(input())
# commands = []
# for t in range(T):
#     commands.append(input())
# # 1. 문자열 길이
# for t in range(T):
#     command = commands[t]
#     N = len(command)
#     out_of_range = False
#     if N != 7:
#         print(0)
#         continue
#     if command[0] == command[2]:
#         print(0)
#         continue
#     str_count = []; str_bitmap = 0b0000000
#     str_count.append(command[0])
#     str_count.append(command[2])
#     for n in range(N):
#         if str_count[0] != command[n] and str_count[1] != command[n]:
#             print(0)
#             out_of_range = True
#             break
#         if str_count[1] == command[n]:
#             # str_bitmap ^= 1 << n
#             str_bitmap = str_bitmap ^ 1 << n
#     if str_bitmap == 0b1101100:
#         print(1)
#     elif out_of_range:
#         continue
#     else:
#         print(0)

T = int(input())
commands = []
for t in range(T):
    commands.append(input())
# 1. 문자열 길이
for t in range(T):
    command = commands[t]
    N = len(command)
    out_of_range = False
    if N != 7:
        print(0)
        continue
    if command[0] == command[2]:
        print(0)
        continue
    str_count = []; count = []
    str_count.append(command[0])
    str_count.append(command[2])
    for n in range(N):
        if str_count[0] != command[n] and str_count[1] != command[n]:
            print(0)
            out_of_range = True
            break
        if str_count[0] == command[n]:
            count.append('0')
        else:
            count.append('1')
    if "".join(count) == "0011011":
        print(1)
    elif out_of_range:
        continue
    else:
        print(0)