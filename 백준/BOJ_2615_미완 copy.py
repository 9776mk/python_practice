from pprint import pprint

field = []
N = 19
black_ = 1
white_ = 2

# 바둑판 입력 받음
for _ in range(N):
   field.append(list(map(int, input().split())))
#pprint(field) 

# field = [
#  [0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 2, 0, 0, 2, 2, 2, 1],
#  [0, 0, 1, 2, 0, 0, 0, 0, 1],
#  [0, 0, 0, 1, 2, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 2, 2, 0, 0],
#  [0, 0, 1, 1, 0, 1, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 2, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0]
#  ]


# 바둑판 델타 탐색
# 4가지 경우
# 1  1   11111    1
# 1   1          1
# 1    1        1
# 1     1      1
# 1      1    1 

# 가장 왼쪽, 혹은 가장 위의 바둑알을 출력해야 하므로
# 우, 하, 우상, 우하 델타 검색이 일어나야함
dx = [1, 0, 1, 1]
dy = [0, 1, -1, 1]

is_found = False

# 모든 바둑판 x,y에 대해서
for x in range(N):
    for y in range(N):
        # 좌표값이 흰색 혹은 검은색 돌일 경우에
        #print(f'델타 탐색 시작 좌표 : {x},{y}')

        if field[x][y] == black_ or field[x][y] == white_:
            # 첫 번째 돌로 설정
            stone_cnt = 1
            
            # 델타 탐색 진행
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                while is_found != True:
                # 새로운 nx, ny가 범위를 벗어나지 않고, 색깔이 같으면 cnt +1 하고 같은 방향으로 계속 진행
                    if -1 < nx < N and -1 < ny < N and field[x][y] == field[nx][ny]:
                        stone_cnt += 1
                        #print(f'델타 탐색 현재 좌표 : {nx},{ny}')
                        
                        # 돌이 5개이면
                        if stone_cnt == 5:
                            # 6목 검사를 해서 6목이 아닌 경우 x, y 를 출력
                            # 6목 검사는 시작한 x,y에서 -델타 탐색 방향과 5목에 해당 되는 곳에서 한 번 더 델타 탐색
                            nx_0, ny_0 = x - dx[i], y - dy[i]
                            nx_6, ny_6 = nx + dx[i], ny + dy[i]
                            #print(f'-1번째 돌 {nx_0}, {ny_0}')
                            #print(f'6번째 돌 {nx_6}, {ny_6}')

                            # 1~5 번째 돌이 다 바둑판 안에 있다면 둘다 바둑판 범위를 벗어나도 괜찮음
                            if not(-1 < nx_0 < N and -1 < ny_0 < N and -1 < nx_6 < N and -1 < ny_6 < N):
                                print(field[x][y])
                                print(x+1, y+1) 
                            
                            # 만약 둘 다 범위안에 있다면 0번째 돌과 6번째 돌을 확인해야 함
                            else:
                                if field[nx_0][ny_0] != field[x][y] and field[nx_6][ny_6] != field[x][y]:
                                    
                                    is_found = True
                                    break



                        nx = nx + dx[i]
                        ny = ny + dy[i]

                    else:
                        break
        if is_found:
            break
    if is_found:
        break