import sys
N = int(sys.stdin.readline())
str_arr = []
for n in range(N):
    buf = sys.stdin.readline()
    buf = buf.replace(" ", "")
    str_arr.append(buf)
    # str_arr.append(input().replace(" ", ""))
for enjoy_str in str_arr:
    enjoy_jumsu = 0
    for string in enjoy_str[:-1]: # enjoy_str[:-1]은 sys.stdin.readline()을 사용할 때만
        enjoy_jumsu += (ord(string) & 0b0111111)
        # enjoy_jumsu += (ord(string) - 64)
    if enjoy_jumsu == 100:
        print('PERFECT LIFE')
    else:
        print(enjoy_jumsu)
