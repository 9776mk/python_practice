T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    total_dis = 0
    cur_spd = 0

    for command in range(N):
        command_list = list(map(int, input().split()))

        # 속도 유지
        if (command_list[0] == 0): 
            total_dis += cur_spd
        # 가속하는 경우
        elif (command_list[0] == 1):
            cur_spd += command_list[1]
            total_dis += cur_spd
        # 감속하는 경우
        else: 
            if cur_spd <= command_list[1]:
                cur_spd = 0
            else:
                cur_spd -= command_list[1]
                total_dis += cur_spd

    print(f'#{test_case} {total_dis}')