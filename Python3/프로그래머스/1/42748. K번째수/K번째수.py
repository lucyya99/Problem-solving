def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sorted_arr = sorted(array[i-1:j])
        answer.append(sorted_arr[k-1])
    return answer