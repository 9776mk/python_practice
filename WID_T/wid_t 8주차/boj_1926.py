from collections import deque

# 출력 함수 정의
def pprint(n):
    for i in n:
        print(i)

# bfs 정의
def bfs(a, b):
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if map_[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
