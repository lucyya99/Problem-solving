def solution(code):
    answer = [] # 문자열 길이 -> O(n)
    mode = True
    for i, s in enumerate(code):
        mode = not mode if s == "1" else mode
        if s == "1":
            continue
        elif mode and i % 2 == 0:
            answer.append(s) # 얘가 문제 / 'abc' + 'cd' => 'abccd' (연산=5번)
        elif not mode and i % 2 != 0:
            answer.append(s) # 얘가 문제
    if len(answer) == 0:
        return "EMPTY"

    return "".join(answer)