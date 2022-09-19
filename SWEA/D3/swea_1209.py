from pprint import pprint

for tc in range(1,11):
    n = int(input())

    matrix = []

    # 100행까지 집어넣기
    for i in range(100):
        matrix.append(list(map(int, input().split())))
    #print(matrix)

    # max값 저장용 변수
    max_ = 0

    # 행의 최댓값
    for i in range(100):
        if sum(matrix[i]) > max_:
            max_ = sum(matrix[i])

    # 열의 최댓값
    # 열의 최댓값을 구하기 위한 임시 변수
    for i in range(100):
        tmp_col = 0
        for j in range(100):
            tmp_col += matrix[j][i]
            
        if tmp_col > max_:
            max_ = tmp_col
    
    # 오른쪽 아래 방향 대각선 합
    tmp_dia_down = 0
    for i in range(100):
        tmp_dia_down += matrix[i][i]
    if tmp_dia_down > max_:
        max_ = tmp_dia_down
    
    # 오른쪽 위 방향 대각선 합
    tmp_dia_down = 0
    for i in range(100):
        tmp_dia_down += matrix[i][99-i]
    if tmp_dia_down > max_:
        max_ = tmp_dia_down

    print(f'#{tc} {max_}')