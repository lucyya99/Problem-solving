def solution(code):
    answer = ''
    mode = True
    for i, s in enumerate(code):
        mode = not mode if s == "1" else mode
        if s == "1":
            continue
        elif mode and i % 2 == 0:
            answer += s
        elif not mode and i % 2 != 0:
            answer += s
    if len(answer) == 0:
        return "EMPTY"

    return answer