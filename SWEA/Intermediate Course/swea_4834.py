T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    digit_list = [0,0,0,0,0,0,0,0,0,0]
    n_number = input()
    max_num = 0
    max_index = 0
    # 입력 받은 글자가 있다면, 해당하는 인덱스에 +1
    for number in n_number:
        digit_list[int(number)] += 1

    # 0부터 9까지 값들을 비교해서, max_num 값을 바꿈
    for i in range(10):
        if digit_list[i] >= max_num:
            max_num = digit_list[i]
            max_index = i
        else:
            continue

    print(f'#{test_case} {max_index} {max_num}')