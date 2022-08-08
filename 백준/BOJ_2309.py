list_ = []
# 난쟁이 키를 list에 입력받음
for _ in range(9):
    list_.append(int(input()))

# 난쟁이 키의 총합 - 100을 저장
gap_ = sum(list_) - 100

# 난쟁이 두 명의
for i in range(8):
    for j in range(i+1, 9):
        # 키를 각각 더해서
        two_sum = list_[i] + list_[j]
        # print(two_sum)

        # 두 명의 키가 총합 - 100과 같다면 각각 리스트에서 제거
        if two_sum == gap_:
            # j를 먼저 제거해야 index 오류가 생기지 않음
            list_.remove(list_[j])
            # print(list_)
            list_.remove(list_[i])
            # print(list_)
            break
    # 난쟁이가 7명이라면 종료
    if (len(list_) == 7):
        break
# 키 순서대로 정렬
list_.sort()

# 하나씩 출력
for num in list_:
    print(num)

# 인데스를 따로 저장해서 출력할 때 그 인덱스를 제외하고 출력