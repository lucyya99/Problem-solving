def solution(prices):
    answer = []
    diff = []
    pop_time = {}
    len_ = len(prices) - 1
    for i, price in enumerate(prices):
        if not diff:
            diff.append(i)
            continue

        if (top_price := prices[diff[-1]]) <= price:
            pass
        else:
            # 들어온 값이 맨 위 값보다 작을 때
            pop_idx = diff[-1]
            # 들어온 값이 맨 위 값보다 클 때까지 pop
            while diff and prices[pop_idx] > price:
                pop_idx = diff.pop()
                pop_time[pop_idx] = i - pop_idx
                if diff:
                    pop_idx = diff[-1]
        diff.append(i)
    
    for i in range(len(prices)):
        if not pop_time.get(i):
            answer.append(len_-i)
        else:
            answer.append(pop_time[i])
    return answer