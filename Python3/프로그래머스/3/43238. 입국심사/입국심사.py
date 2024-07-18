def solution(n, times):
    left = 1                # 최소 사람수
    right = max(times) * n  # 최대 사람수
    # 가능한 사람 수 찾기
    while left <= right:
        mid = (left + right) // 2

        people = 0
        
        for time in times:
            people += mid // time
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer