N = int(input())

a = []
for _ in range(N):
    a.append(tuple(map(int, input().split(" "))))
a = sorted(a, key=lambda x: (x[1], x[0]))

for n in a:
    print(n[0], n[1])