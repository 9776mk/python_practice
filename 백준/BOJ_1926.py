def pprint(arr):
    for i in range(len(arr)):
        print(arr[i])

# 세로 가로 입력
# 공백을 기준으로 나뉘어진 숫자 2개
n, m = list(map(int, input().split()))

# 빈 그래프 생성
graph = []
# n번 만큼 이ㅣㄹ차원 그래프를 입력 & 추가
for _ in range(n):
    graph.append(list(map(int, input().split())))


# 방문 표시 이차원 그래프
visited = []
# 행의 개수 n 만큼 2차원 리스트 생성
for _ in range(n):
    visited_list = [False] * m
    visited.append(visited_list)

# 상 하 좌 우 델타 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


세로, 가로 = list(map(int, input().split()))

for sy in range(n):
    for sx in range(m):
        # [sy][sx] 
        # DFS 실행
        if not visited[sy][sx] and graph[sy][sx] == 1:
            
            # 시작점을 stack append
            stack = []
            stack.append([sy,sx])
            # 시작점을 방문처리
            visited[sy][sx] = True

            while stack:
                y, x = stack.pop()
                
                # 델타 탐색 시행
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    # 조건 1, 2, 3
                    # 조건 1. 범위
                    if not (-1 < ny < n and -1 < nx < m):
                        continue

                    # 조건 2. 방문 확인
                    if visited[ny][nx] == True:
                        continue

                    # 조건 3. 좌표의 값이 1
                    # 그림이어야 한다.
                    if graph[ny][nx] != 1:
                        continue

                    # 조건을 다 통과하면
                    # stack에 값을 넣고
                    # 방문 처리
                    stack.append((ny,nx))
                    visited[ny][nx] = True