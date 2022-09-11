def solution(s):    
    # 반복 횟수
    cnt = 0

    # 제거된 0 개수
    cnt_0 = 0
    cnt_1 = 0

    # s가 1이 될 때까지
    while s != '1':
        # 반복횟수 1 추가
        cnt += 1
        # 제거한 0 개수 추가
        cnt_0 += s.count('0')
        # 1의 개수
        cnt_1 = s.count('1')

        s = format(cnt_1, 'b')

    answer = [cnt, cnt_0]
    return answer

print(solution("110010101001"))
