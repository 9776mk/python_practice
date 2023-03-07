from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    list_.append(graph[a][b])
    count = 1
    num_[a][b] = count

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == False:
                print(graph[nx][ny])
                visited[nx][ny] = True

                if graph[nx][ny] not in list_:
                    list_.append(graph[nx][ny])
                    queue.append((nx, ny))

    return len(list_)


# R, C = map(int, input().split())
R, C = 5, 5
# graph = [list(str(input())) for _ in range(R)]
graph = [
    ["I", "E", "F", "C", "J"],
    ["F", "H", "F", "K", "C"],
    ["F", "F", "A", "L", "F"],
    ["H", "F", "G", "C", "F"],
    ["H", "M", "C", "H", "H"],
]
visited = [[False] * C for _ in range(R)]
list_ = []
num_ = [[0] * C for _ in range(R)]

print(bfs(0, 0))
print(num_)
