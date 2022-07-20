T = int(input())

for test_case in range(1, T+1):
    case_num = int(input())
    score_list = list(map(int, input().split()))
    freq_max = 0
    freq_num = 0

    for score in score_list:
        if score_list.count(score) >= freq_max:
            freq_max = score_list.count(score)
            freq_num = score
        else:
            continue

    print(f'#{test_case} {freq_num}')