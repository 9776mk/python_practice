T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())    
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))

    # n, m = 3, 5
    # list_n = [1, 5, 3]
    # list_m = [3, 6, -7, 5, 4]

    short_, long_ = min(n,m), max(n,m)

    # 더 짧은 리스트를 저장
    if n < m:
        short_list, long_list = list_n, list_m
    else:
        short_list, long_list = list_m, list_n

    # 반복 횟수는 0부터 긴 리스트 길이 - 짧은 리스트 길이 + 1
    rep_ = long_ - short_ + 1

    # 합들을 저장할 리스트
    sum_list = []

    # 0부터 ~ 긴 리스트 - 짧은 리스트 + 1의 범위에서
    for i in range(rep_):
        # 합을 저장할 변수 sum_ 선언, 새로운 반복을 할 때마다 초기화
        sum_ = 0

        # 짧은 리스트의 길이만큼 반복
        for j in range(short_):
            # 짧은 리스트는 0 ~ 3(short_)까지 반복
            # 긴 리스트는 0 ~ 3(short_), 1 ~ 4, 2 ~ 5, ... 
            sum_ += long_list[i+j] * short_list[j]
        sum_list.append(sum_)

    print(f'#{test_case} {max(sum_list)}')