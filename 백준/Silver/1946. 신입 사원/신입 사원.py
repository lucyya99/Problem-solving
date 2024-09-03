from sys import stdin

T = int(stdin.readline())
for t in range(T):
    N = int(stdin.readline())
    scores = []

    for n in range(N):
        doc, interview = map(int, stdin.readline().split())
        scores.append((doc, interview))

    # 서류 점수를 기준으로 정렬
    scores.sort()

    # 서류 점수에 따라 정렬된 상태에서 인터뷰 점수를 비교하며 선택
    min_interview_score = scores[0][1]
    length = 1  # 첫 번째 지원자는 무조건 선택됨

    for i in range(1, N):
        if scores[i][1] < min_interview_score:
            length += 1
            min_interview_score = scores[i][1]

    print(length)


    # 일단 doc 기준으로 sorting
    # interview 기준으로 다음값보다 작으면 -1

    # doc ranking 1위랑 interview ranking -1위랑
    #     3      2      1      5
    # [1, 4] [2, 3] [3, 2] [4, 1](x) [5, 5]
    # [1, 4](x) [2, 5](x) [3, 6] [4, 2](x) [5, 7] [6, 1](x) [7, 3]
