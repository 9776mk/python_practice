def solution(p):
    p.sort()
    # 1. 문자열 정렬은 숫자 정렬과 다르게  사전식으로 정렬한다.
    for i in range(len(p)-1): 
        # 2. 사전식 정렬이므로, p[i]와 p[i+1]만 비교를 해도 된다.
        # 또한 p[i+1] 전체가 아닌 p[i]의 길이만큼만 확인을 해서 똑같으면 return으로 값을 반환함과 동시에 종료한다.
        if p[i] == (p[i+1])[:len(p[i])] : 
            return False

    return True