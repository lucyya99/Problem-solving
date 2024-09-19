from sys import stdin
a = stdin.readline().strip()
b = stdin.readline().strip()

LCS = [[0 for j in range(len(a)+1)] for i in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i - 1] == a[j - 1]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[len(b)][len(a)])

# result = []

# i, j = len(b), len(a)


# while (i > 0 and j > 0):
#     diff = LCS[i][j]
    
#     if diff == LCS[i - 1][j]:
#         i -= 1
#     elif diff == LCS[i][j - 1]:
#         j -= 1
#     else:
#         result.append(a[j - 1])
#         i -= 1
#         j -= 1


# print("".join(result[::-1]))