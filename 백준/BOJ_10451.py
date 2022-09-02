def dfs(start):
  stack = [start] # 돌아갈 곳을 기록
  visited[start] = True # 시작 정점 방문 처리

  while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
    cur = stack.pop() # 현재 방문 정점(후입선출)

    for adj in graph[cur]: # 인접한 모든 정점에 대해
       if not visited[adj]: # 아직 방문하지 않았다면
            visited[adj] = True # 방문 처리
            stack.append(adj) # 스택에 넣기


T = int(input())

for test_case in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    # print(graph)

    n_list = list(map(int, input().split()))
    #print(n_list)

    for i in range(N):
        graph[i+1].append(n_list[i])
    #print(graph)

    visited = [False] * (N + 1)

    cnt = 0
    # 1부터 N까지 돌려서
    for i in range(1, N+1):
        # 방문하지 않았다면
        if visited[i] == False:
            # dfs 실행하고
            dfs(i)
            # 횟수 + 1
            cnt += 1
        else:
            continue

    print(cnt)