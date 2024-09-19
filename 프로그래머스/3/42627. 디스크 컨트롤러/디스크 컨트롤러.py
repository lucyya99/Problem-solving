import heapq

def solution(jobs):
    jobs.sort()
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    # T = 작업이 요청되는 시간 (최대) [0, 1] [999, 1] : T - n
    # (T+n) * (nlogn)
    while i < len(jobs): # T + n
        for j in jobs: # n
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]]) # O(logn)
        
        if len(heap) > 0:
            current = heapq.heappop(heap) # O(logn)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    
    return int(answer / len(jobs))