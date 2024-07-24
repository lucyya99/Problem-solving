from sys import stdin, stdout

N = stdin.readline()
A = list(map(int, stdin.readline().split()))
n = len(A)
answer = [-1 for _ in range(n)]
stack = []  # stack 내부에는 단조 감소하는 수만 있다
for i, v in enumerate(A):
    while stack and stack[-1][1] < v:   # 입력값보다 맨 위값이 클 때
        pop_i, pop_v = stack.pop()
        answer[pop_i] = v
    stack.append((i, v))

for a in answer:
    print(a, end=" ")