T = int(input())


for test_case in range(T):
    over_avg = 0
    percent_std = 0.0
    sum = 0
    score_num = list(map(int, input().split()))
    
    # print(score_num, type(score_num))
    # print(score_num[1], type(score_num[1]))

    for i in range(1, len(score_num)):
        sum += score_num[i]
    
    avg = sum / (score_num[0])
    # print(avg)
    for i in range(1, len(score_num)):
        if score_num[i] > avg:
            over_avg += 1

    percent_std = (over_avg / score_num[0])*100

    print(f'{percent_std:.3f}%')