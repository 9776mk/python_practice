from collections import deque

# ???? 정점 번호가 작은 것 방문 ????


def dfs(start):
  stack = [start] # 돌아갈 곳을 기록
  visited_dfs[start] = True # 시작 정점 방문 처리

  while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
    cur = stack.pop() # 현재 방문 정점(후입선출)
    print(cur, end=" ")

    for adj in graph[cur]: # 인접한 모든 정점에 대해
       if not visited_dfs[adj]: # 아직 방문하지 않았다면
            visited_dfs[adj] = True # 방문 처리
            stack.append(adj) # 스택에 넣기

    # pop은 제일 오른쪽을 뽑으므로, 내림차순으로 정렬해서 정점 번호가 작은 것부터 방문.
    stack.sort(reverse=True)
    # 1,2,3,4
    # print(stack)

def bfs(start):
  # 큐 (queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited_bfs[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기
    cur = queue.popleft()
    print(cur, end=' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for adj in graph[cur]:
      if not visited_bfs[adj]:
        queue.append(adj)
        visited_bfs[adj] = True

N, M, V = map(int, input().split())

# 그래프가 1부터 시작하므로 0 ~ N까지 생성한 후 1~N까지 적용
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(V)
print()
bfs(V)