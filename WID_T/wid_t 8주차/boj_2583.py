from collections import deque

def pprint(n):
    for i in n:
        print(i)

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    area = 1

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                # 값이 0일때 bfs 실행
                if list_[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area += 1
    return area

# M : 세로, N : 가로, K : 직사각형 개수
M, N, K = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

list_ = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
list_area = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            list_[j][i] = 1
cnt = 0
for i in range(M):
    for j in range(N):
        if list_[i][j] == 0 and visited[i][j] == False:
            list_area.append(bfs(i,j))
            cnt += 1


list_area.sort()
print(cnt)
for i in list_area:
    print(i, end=" ")