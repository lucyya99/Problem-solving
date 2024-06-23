# import sys
# N, K = sys.stdin.readline().split()
# N = int(N); K = int(K)
# A = list(map(int, sys.stdin.readline().split()))
# capacity = 0
#
# for a in A:
#     # if a&1 == 0:
#     if a%2 == 0:
#         capacity += a // 2
#     else:
#         capacity += a//2 + 1
#
# if capacity >= N:
#     print('YES')
# else:
#     print('NO')

# import sys
# N, K = sys.stdin.readline().split()
# N = int(N); K = int(K)
# A = list(map(int, sys.stdin.readline().split()))
#
# for a in A:
#     N -= (a+1)//2
# if N <= 0:
#     print('YES')
# else:
#     print('NO')

import sys
N, K = sys.stdin.readline().split()
N = int(N); K = int(K)
A = list(map(int, sys.stdin.readline().split()))
capacity = 0
for a in A:
    capacity += (a+1)//2

if capacity >= N:
    print('YES')
else:
    print('NO')

# import sys
# import math
# N, K = sys.stdin.readline().split()
# N = int(N); K = int(K)
# cnt=0
# tmp=list(map(int,sys.stdin.readline().split()))
# for i in tmp:
#     cnt+= math.ceil(i/2)
# if N>cnt: print("NO")
# else: print("YES")