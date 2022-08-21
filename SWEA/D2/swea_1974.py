T = int(input())
num_ = {1,2,3,4,5,6,7,8,9}

for test_case in range(1, T+1):
    sudoku = []
    for _ in range(9):
        list_ = list(map(int, input().split()))
        sudoku.append(list_)
    # 숫자가 제대로 들어가 있는지 확인하기 위한 변수
    is_ok = True

    # 행 검증
    for i in range(9):
        if set(sudoku[i]) != num_:
            is_ok = False
            break

    # 열 검증
    for i in range(9):
        list_col = []
        for j in range(9):
            list_col.append(sudoku[j][i])

        if set(list_col) != num_:
            is_ok = False
            break

    # 3 x 3 검증
    for i in range(0,9,3):
        for j in range(0,9,3):
            list_9 = []
            for k in range(3):
                for l in range(3):
                    #print(sudoku[i+k][j+l])
                    list_9.append(sudoku[i+k][j+l])
            if set(list_9) != num_:
                is_ok = False
                break
            
    # 한 번도 False로 바뀐 적이 없다면 1, 있다면 0 출력
    if is_ok:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')