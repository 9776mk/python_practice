for _ in range(1):
    # 숫자를 str형으로 입력받음
    number = input()
    
    # 제일 첫 글자를 임시 변수로 설정
    tmp_num = number[0]
    
    # 제일 많은 글자를 세기 위한 변수 설정
    max_cnt = 0

    cnt = 1

    for i in range(1,8):
        # 현재값이 이전 값과 같으면
        if number[i] == tmp_num:
            # 하나 더 추가
            cnt += 1
            # 현재값이 이전 값과 같은데 마지막이라면
            if i == 7:
                if cnt > max_cnt:
                    max_cnt = cnt

        # 현재값이 이전 값과 다르면
        elif number[i] != tmp_num:
            tmp_num = number[i]

            if cnt > max_cnt:
                max_cnt = cnt

            cnt = 1
    
    print(max_cnt)