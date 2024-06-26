def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break
    
    if (l := k-len(answer)) >= 0: # 4-2 = 2 > 0
        for _ in range(l):
            answer.append(-1)
    return answer