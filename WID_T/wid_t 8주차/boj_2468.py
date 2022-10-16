from collections import deque

def pprint(n):
    for i in n:
        print(i)

def bfs(a,b,c):
    queue = deque()
    queue.append((a,b))
    area = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
               if list_[nx][ny] > c and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return area

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

n = int(input())
list_ = []
list_safe = []

for _ in range(n):
    list_.append(list(map(int, input().split())))

# 2차원 리스트에서 최솟값과 최댓값 구할 때 map을 활용
min_ = min(map(min, list_))
max_ = max(map(max, list_))

#
if min_ == max_:
    print(1)
else:    
    for i in range(min_, max_):
        cnt = 0
        visited = [[False] * n for _ in range(n)]
        for j in range(n):
            for k in range(n):
                # 해당 좌표가 i보다 크고, 방문하지 않았다면
                if list_[j][k] > i and visited[j][k] == False:
                    bfs(j,k,i)
                    cnt += 1
        list_safe.append(cnt)
    print(max(list_safe))