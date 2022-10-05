def solution(participant, completion):
    dict_ = {}
    
    # 참가자로 딕셔너리 생성
    for person in participant:
        dict_[person] = dict_.get(person, 0) + 1

    # 완주자 리스트에 이름이 있으면 dict_의 키값을 뺌
    for person in completion:
        dict_[person] = dict_.get(person) - 1

    # 딕셔너리의 값이 0이 아니면 answer에 키 넣기
    for k, v in dict_.items():
        if v != 0:
            answer = k
    return answer