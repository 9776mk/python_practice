from collections import deque

def bfs(n, k):
    queue = deque()
    queue.append(n)
    cnt = 0
    while queue:
        x = queue.popleft()
        visited[x] = True
        cnt_[x] = cnt

        # x가 k값과 같다면 출력
        if x == k:
            return cnt_[x]
        # x가 k값과 다르다면
        else:
            if x-1 >=0 and not visited[x-1]:
                queue.append(x-1)
                visited[x-1] = True
                cnt_[x-1] = cnt_[x] + 1
            if x+1 <= 100000 and not visited[x+1]:
                queue.append(x+1)
                visited[x+1] = True
                cnt_[x+1] = cnt_[x] + 1
            if 2*x <= 100000 and not visited[2*x]:
                queue.append(2*x)
                visited[2*x] = True
                cnt_[2*x] = cnt_[2*x] + 1


# N, K = map(int, input().split())
N, K = 5, 17
visited = [False] * (100000)
cnt_ = [0] * (100000)


print(bfs(N, K))