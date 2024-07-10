import re
def ordering(x): # tail에 대한 정렬은 없음.
    re_str = re.search(r'\d+', x)
    head = x[:re_str.start()].lower()
    number = int(re_str.group())
    return head, number

def solution(files):
    return sorted(files, key=ordering)