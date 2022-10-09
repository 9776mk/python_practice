from collections import deque
# bfs 선언
def bfs(a,b):
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        # 사방탐색 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 사방탐색이 범위를 벗어나지 않으면
            if 0 <= nx < n and 0 <= ny < m:
                # 0이 아니고, 방문을 하지 않았다면
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

                # 사방탐색이 진행된 부분이 0, 즉 바다라면
                elif graph[nx][ny] == 0:
                    # 사방탐색 진행을 시작한 좌표의 count좌표에 1추가
                    count[x][y] += 1

    return 1

# 사용자로부터 입력 받기
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 사방탐색용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# deque로 선언
queue = deque()

# 날짜와 분리 여부 확인용 변수 선언
day = 0
is_divided = False

# 빙산이 분리될때까지 돌아줌
while True:
    # 방문 리스트와 바다 갯수용 리스트 생성
    visited = [[False] * m for _ in range(n)]
    count = [[0] * m for _ in range(n)]
    # 결과 리스트에 bfs 리턴 값을 추가해 bfs 횟수를 카운트 할 수 있음
    result = []

    # bfs가 실행되는 횟수를 result에 저장
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))

    # 빙산을 깍아줌           
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    # result의 길이가 0인 경우, 즉 한 번도 bfs가 일어나지 않았다면
    if len(result) == 0:
        break

    # result의 길이가 2이상인 경우라면
    elif len(result) >= 2: # 빙산이 분리되면 break
        is_divided = True
        break
    # 전부 실행했을 때 break로 빠져나가지 않았다면 day 하루 추가
    day += 1

# 빙산이 분리가 되었다면
if is_divided:
    # 날짜 출력        
    print(day)
# 빙산이 분리가 되지 않았다면
else:
    # 0 출력
    print(0)