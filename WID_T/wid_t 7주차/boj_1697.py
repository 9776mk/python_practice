from collections import deque

def dfs(n, k):
    cnt = 1
    queue = deque([n])
    visited[n] = 1

    while queue:
        x = queue.popleft()
        nx = 2 * x
        # 2*x 한 것이 k보다 작으면
        if nx < k and visited[nx] != 1:
            # 2x로 이동
            cnt += 1
            # 방문 처리
            visited[nx] = 1
            # 스택에 쌓기
            queue.append(nx)
        # 2배 한 것이 k보다 크면
        else:





n, k = map(int, input().split())
cnt = 0

graph = [0] * k
visited = [0] * k

