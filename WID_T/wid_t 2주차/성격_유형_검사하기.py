def solution(survey, choices):
    # 지표의 값을 위한 dict 선언
    dict_ = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 시행할 갯수 구하기
    n = len(survey)

    # 처음부터 끝까지 시행
    for i in range(n):
        # 앞 뒤 글자 나누기
        front_ = survey[i][0]
        back_ = survey[i][1]
        
        # 해당하는 점수 더하기
        score = abs(4 - choices[i])
        if choices[i] < 4:
            dict_[front_] = dict_.get(front_) + score
        elif choices[i] > 4:
            dict_[back_] = dict_.get(back_) + score

    # 반영하기

    print(dict_)    

    answer = ''

    if dict_['R'] >= dict_['T']:
        answer += 'R'
    elif dict_['R'] < dict_['T']:
        answer += 'T'

    if dict_['C'] >= dict_['F']:
        answer += 'C'
    elif dict_['C'] < dict_['F']:
        answer += 'F'

    if dict_['J'] >= dict_['M']:
        answer += 'J'
    elif dict_['J'] < dict_['M']:
        answer += 'M'
        
    if dict_['A'] >= dict_['N']:
        answer += 'A'
    elif dict_['A'] < dict_['N']:
        answer += 'N'

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))