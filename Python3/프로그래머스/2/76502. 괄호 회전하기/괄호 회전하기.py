def solution(s):
    answer = 0

    s = list(s)
    for i in range(len(s)):
        # rotate
        temp = s[-1]
        #if temp == "}" or temp == ')' or temp == "]":
        #    continue
        s.insert(0, temp)
        s.pop()

        stack = []
        for p in s:
            if not stack:
                stack.append(p)
                continue
            
            if stack[-1] == '(' and p == ')':
                stack.pop()
            elif stack[-1] == '[' and p == ']':
                stack.pop()
            elif stack[-1] == '{' and p == '}':
                stack.pop()
            else:
                stack.append(p)
        
        if not stack:
            answer += 1

    return answer