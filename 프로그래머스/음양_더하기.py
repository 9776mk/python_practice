def solution(absolutes, signs):
    # 최종 답을 구할 answer 선언
    answer = 0
    # 실행횟수를 구하기 위한 len_list
    len_list = len(absolutes)


    # signs의 원소가 True이면 absolutes 원소를 더하고 False이면 뺀다.
    for i in range(len_list):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer