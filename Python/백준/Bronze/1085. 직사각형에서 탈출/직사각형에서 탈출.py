import sys
x, y, w, h = map(int, sys.stdin.readline().strip().split(" "))
print(min([w-x, h-y, x, y]))