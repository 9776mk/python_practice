def solution(nums):
    dict_ = {}

    # 딕셔너리에 폰켓몬 집어넣기
    for num in nums:
        dict_[num] = dict_.get(num, 0) + 1

    len_num = int((len(nums))/2)
    len_dict = len(dict_)

    # 만약 가져갈 수 있는 종류보다 폰켓몬 종류가 더 많다면
    if len_dict >= len_num:
        # 가져갈 수 있는 최대한 가져감
        answer = len_num
    # 만약 가져갈 수 있는 종류가 폰켓몬 종류가 더 적다면    
    else:
        # 폰켓몬 종류만큼 가져감
        answer = len_dict

    return answer