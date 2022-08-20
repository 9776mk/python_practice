# 오목

'''
# 우 하 우상 우하
dy = [0, 1, -1, 1]
dx = [1, 0, 1, 1]


BALCK = 1
WHITE = 2
N = 19

board = []


# 오목판 상황 입력
for _ in range(N):
    하나의 행을 입력
    temp_list = list(map(int, input().split()))
    board.append(temp_list)

# pprint(board)

answer = 0

# 이중 반복문
for y in range(N):
    for x in range(N):
      # 검은색돌이나 흰색돌일때만 델타 탐색을 수행
      if board[y][x] == BLACK or board[y][x] == WHITE




        # 델타 탐색
        for d in  range(4):
            ny = y +dy[d]
            nx = x +dx[d]

            while True:
                # 인덱스 조건
                if not(-1 < ny < N and -1 < nx < N):
                    break  
                # 같은 색(값) 돌인지 확인하는 조건
                if (not(board[y][x]) == board[ny][ny]):
                    break
                # 같은 값이고 범위를 벗어나지 않으면
                stone_count += 1


                # 같은 방향 다음 좌표를 탐색
                ny = ny +dy[d]
                nx = nx +dx[d]
          
             # 돌의 개수가 5개라면
            if stone_count == 5:
              prev_y = y - dy[d]
              prev_x = x - dx[d]

              # 육목인지 판단
              # 조건 1. 이전좌표가 범위를 벗어나면 오목
              # if not(-1 < prev_x < N and -1 < prev_x < N)
              # 조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
              # if board[y][x] != board[prev_y][prev_x]:
              # 조건 1 혹은 조건 2를 만족하면 오목
              if not(-1 < prev_x < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:
                answer = board[y][x]
                # 현재 돌의 색 출력
                print(board[y][x])
              # 현재 돌의 좌표 출력
                print(y + 1, x + 1)

if answer ==0:
  print(answer)



'''

























N , M = map(int, input().split())

maze_ = []

for _ in range(N):
  maze_.append(input())

# print(maze_)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt = 0




























'''
import sys

input = sys.stdin.readline

# 4방향 탐색 세로,가로, 오른쪽아래 대각선 오른쪽 위 대각선
dx = [0, 1, -1, 1]
dy = [1, 0,  1, 1]
def check():
		# 오목판 크기
    for x in range(19):
        for y in range(19):
						# 백돌 or 흑돌 이면
            if maps[x][y]:
								# 위에서 언급한 4방향 탐색 진행
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
										# 몇 목인지 세기 위한 cnt변수
                    cnt = 1
										# 범위를 벗어나면 다시 돌아가~
                    if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
                        continue
										# 범위안에 있고 기존에 시작했던 진짜 했던 돌 인지 아닌지 판단하면서 while문 돌리기
                    while 0 <= nx < 19 and 0 <= ny < 19 and maps[x][y] == maps[nx][ny]:
												# nx, ny가 같은돌이니까 다시 cnt += 1
                        cnt += 1
												# if cnt == 5이면 x - dx[i] y - dy[i] 이 곳과 nx + dx[i] ny + dy[i] 두곳을
												# 확인 해줘야 한다.
                        if cnt == 5:
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and maps[nx][ny] == maps[nx+dx[i]][ny+dy[i]]:
                                break
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and maps[x][y] == maps[x - dx[i]][y - dy[i]]:
                                break
                            return maps[x][y], x + 1, y + 1
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1
maps = [list(map(int, input().split())) for _ in range(19)]

color, x, y = check()
if not color:
    print(color)
else:
    print(color)
    print(x, y)
'''