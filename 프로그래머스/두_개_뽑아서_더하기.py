def solution(numbers):
    added_list = []

    # 0 ~ 끝-1
    for i in range(len(numbers)-1):
        # i+1 부터 끝까지
        for j in range(i+1, len(numbers)):
            added_list.append(numbers[i]+numbers[j])

    answer = []
    # set으로 중복을 없앤 후 리스트로 변환
    answer = list(set(added_list))
    answer.sort()

    return answer

    # [2,1,3,4,1] -> [2,3,4,5,6,7]