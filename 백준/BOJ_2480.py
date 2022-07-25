# 입력을 list로 받은 뒤 오름차순으로 sort로 정렬.
# 만약 첫번째와 세번째가 같다면 세개 다 동일
# 두번째는 각각 비교
# 세 번째는 모두 다른 경우 비교
# 조건에 따라 계산해보기

dice = list(map(int, input().split()))
dice.sort()

if dice[0] == dice[2]:
    print(10000+dice[2]*1000)
elif dice[0] == dice[1] or dice[1]==dice[2]:
    print(1000+dice[1]*100)
else:
    print(dice[2]*100)