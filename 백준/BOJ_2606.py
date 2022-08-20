from pprint import pprint

# DFS - 스택

# 컴퓨터 수, 컴퓨터 쌍의 수 입력 
n = int(input())
m = int(input())
# n = 7
# m = 6

# 네트워크 쌍 저장 리스트
list_ = [[] for _ in range(n+1)]

# 그래프 입력 받은 후 쌍 추가
# 무방향 그래프이므로 양쪽 다 추가
for _ in range(m):
    a, b = map(int, input().split())
    list_[a].append(b)
    list_[b].append(a)

# pprint(list_)

# 방문 여부를 위한 리스트 생성
visited = [False] * (n+1)

def dfs(start):
  stack = [start] # 돌아갈 곳을 기록
  visited[start] = True # 시작 정점 방문 처리

  while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
    cur = stack.pop() # 현재 방문 정점(후입선출)

    for adj in list_[cur]: # 인접한 모든 정점에 대해
       if not visited[adj]: # 아직 방문하지 않았다면
            visited[adj] = True # 방문 처리
            stack.append(adj) # 스택에 넣기

dfs(1)

print(visited.count(True)-1)