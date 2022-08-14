from pprint import pprint

# 미로 탐색
n, m = map(int, input().split())

# 미로를 입력 받음
miro=[]
for _ in range(n):
    miro.append(list(map(int, input())))
# print(miro)

# miro = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

# 미로 방문용 리스트 생성
visited = [[False] * m for _ in range(n)]

# 칸수용 리스트
dist_ = [[0] * m for _ in range(n)]

# 델타 검색
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 초기 좌표 설정
cur = [0, 0]
dist_[cur[0]][cur[1]] = 1
visited[cur[0]][cur[1]] = True
# print(dist_)

# 스택에 현재 좌표를 집어넣고 
stack = [cur]

# 스택이 비어 있지 않으면 반복
while stack:
    # 현재 좌표에서 델타 탐색을 해서
    cur = stack.pop()

    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        # print(cur)
        # 인덱스를 벗어나지 않고
        if -1 < nx < n and -1 < ny < m:
            # 방문하지 않았을 때
            if visited[nx][ny] == False:
                # 방문한 것으로 만들고
                visited[nx][ny] = True
                # 만약 그 값이 1이라면
                if miro[nx][ny] == 1:
                    # 현재까지의 거리에 +1 해서 기록
                    dist_[nx][ny] = dist_[cur[0]][cur[1]] + 1
                    # 현재 좌표를 다음 좌표로 설정
                    stack.append([nx,ny])
                    print(stack)
            # 만약 끝에 도달했는데 스택이 비어있지 않다면 pop

pprint(visited)
pprint(dist_)
print(dist_[n-1][m-1])