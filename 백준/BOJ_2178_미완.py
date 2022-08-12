# 미로 탐색
n, m = map(int, input().split())

# 미로를 입력 받음
miro=[]
for _ in range(n):
    miro.append(list(map(int, input())))

# 미로 방문용 리스트 생성
visited = [[False] * m for _ in range(n)]

# 칸수용 리스트
dist_ = [[0] * m for _ in range(n)]

# 델타 검색
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 좌표 설정
x, y = 0, 0

# 계속 반복
while True:
    stack = [(x,y)]
    

    # 델타 탐색으로 새로운 좌표 생성
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스를 벗어나지 않을 때
        if -1 < nx < n and -1 < ny < m:
            # 새로운 좌표가 1이면
            if miro[nx][ny] == 1:
                stack.