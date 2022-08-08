from pprint import pprint

n = int(input())
mine_ = []
mine_ = [list(str(input())) for _ in range(n)]
input_ = [list(str(input())) for _ in range(n)]

result_ = [['.'] * n for _ in range(n)]

# 8방향 델타 탐색값 설정
# 좌상      상       우상
#(0,0)    (0, 1)    (0, 2)
# 좌      탐색기준    우
#(1,0)    (1,1)     (1,2)           
# 좌하      하       우하
#(2,0)    (2,1)     (2,2)

#    좌상 상 우상 좌 우 좌하 하 우하
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 지뢰 발견 여부
is_founded = False

for r in range(n):
    for c in range(n):
        # [r][c] 마다 폭탄 개수의 합을 구해줘야 하므로 
        sum_ = 0

        # input_ list의 값이 x이고, 해당 인덱스에 폭탄이 없다면
        if input_[r][c] == 'x' and mine_[r][c] == '.':
            # 범위를 벗어나지 않게 주변 탐색 후 
            for i in range(8):
                new_x = r + dx[i]
                new_y = c + dy[i]

                if 0 <= new_x < n and 0 <= new_y < n:
                    # 주변 탐색시 폭탄을 발견한다면
                    if mine_[new_x][new_y] == '*':
                        # 폭탄 개수에 +1
                        sum_ += 1
            # 주변을 다 둘러봤다면 결과리스트에 반영
            result_[r][c] = str(sum_)

        # input_ 의 list의 값이 x이고, 해당 인덱스에 폭탄이 있다면
        # 효율성을 위해 지뢰가 발견될 때마다 실행하는 것이 아닌
        # is_founded = True / False를 활용해서
        # 지뢰가 발견되면 True로 바꾼 후 출력에 반영할 것!
        # 반영 완료
        elif input_[r][c] == 'x' and  mine_[r][c] == '*' :
            is_founded = True
            '''
            for i in range(n):
                for j in range(n):
                    # 모든 폭탄이 있는 위치를
                    if mine_[i][j] == '*':
                        # 결과리스트에 반영
                        result_[i][j] = '*'
            '''

if is_founded == True:
    for i in range(n):
        for j in range(n):
            # 모든 폭탄이 있는 위치를
            if mine_[i][j] == '*':
                # 결과리스트에 반영
                result_[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(result_[i][j], end='')
    print()