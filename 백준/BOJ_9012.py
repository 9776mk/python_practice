N = int(input())

for _ in range(N):
    str_ = input()
    vps_list = []
    is_vps = True

    # 입력받은 문자열에 대해
    for str in str_:
        # 만약 문자열이 '(' 라면 vps_list에 추가
        if str == '(':
            vps_list.append(str)
        # 문자열이 ')'일 때
        else:
            # vps_list가 0이 아니면, vps_list에서 pop
            if len(vps_list) != 0:
                vps_list.pop()
            # vps_list가 이미 0이라면, 즉 ')'가 더 많으므로 중지하고 Fasle로 바꿈
            else:
                is_vps = False
                break
    # len(vps_list)가 0이 아닌 경우는 '('의 갯수가 더 많은 경우
    if is_vps == True and len(vps_list) == 0:
        print('YES')
    else:
        print('NO')