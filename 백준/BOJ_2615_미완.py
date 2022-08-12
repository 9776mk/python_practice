from pprint import pprint

baduk = []
N = 19
black_ = 1
white_ = 2

# 바둑판 입력 받음
for _ in range(N):
    baduk.append(list(map(int, input().split())))
# pprint(baduk) 

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

# 모든 바둑판 x,y에 대해서
for x in range(N):
    for y in range(N):
        # 좌표값이 흰색 혹은 검은색 돌일 경우에
        if baduk[x][y] == black_ or baduk[x][y] == white_:
            # 첫 번째 돌로 설정
            stone_cnt = 1

            # 델타 탐색 진행
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 새로운 nx, ny가 범위를 벗어나지 않으면
                if -1 < nx < N and -1 < ny < N:

                    # 반복문 진행
                    while True:
                        if baduk[x][y] == 
