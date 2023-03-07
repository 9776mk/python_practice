# 연결 요소의 개수 = 연결되지 않은 것들
# dFS를 한 번 돌려서 연결된 것들은 True, 연결되지 않으면 False
# False인 원소중 하나를 골라 BFS를 돌려 연결되면 True, 연결되지 않으면 False 카운트 +1
# True가 없어질 떄까지 반복


# def dfs(start):
#     # 시작하는 노드를 스택에 넣고
#     stack = [start]
#     # 방문 처리
#     visited[start] = True

#     # 스택이 비어 있지 않은 동안
#     while stack:
#         # stack에서 꺼낸 값을 현재 값으로 설정
#         cur = stack.pop()

#         # list_[cur]에 있는 인접값들을 보고
#         for adj in list_[cur]:
#             # 인접값들을 방문하지 않았다면
#             if not visited[adj]:
#                 visited[adj] = True
#                 stack.append(adj)


# # 정점 개수 n, 간선 개수 m 입력
# n, m = map(int, input().split())

# # 각 정점마다 간선을 입력할 간선 리스트 선언
# # 1부터 시작하므로 정점 개수 +1
# list_ = [[] for _ in range(n + 1)]

# # 방문을 기록할 리스트 선언
# visited = [False] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     list_[a].append(b)
#     list_[b].append(a)

# cnt = 0

# # visited[i]에서 False가 사라질 때까지 반복
# # visited가 반영이 될까? - 반영 됨.
# # 변수에 대한 공부가 필요할 것 같음
# for i in range(1, n + 1):
#     if visited[i] == False:
#         dfs(i)
#         cnt += 1
#     else:
#         continue

# print(cnt)


import sys

# 재귀 횟수를 늘려줌
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 노드 개수, 에지 개수 입력받음
n, m = map(int, input().split())

# 인접행렬 저장 리스트
# 보통 n개의 원소를 가진 리스트의 범위를 range(n), 0 ~ n-1으로 총 n개 생성 하지만
# 에지의 경우 1부터 시작하므로 편의성을 위해 0 ~ n까지 생성후 1 ~ n 까지 사용하기 위함
A = [[] for _ in range(n + 1)]

# 방문 리스트
# 에지가 1 ~ n까지 이므로 n까지 선언
visited = [False] * (n + 1)


def DFS(v):
    # 먼저 방문 처리를 한 후
    visited[v] = True
    # 해당하는 노드를 돌아서
    for i in A[v]:
        # 방문하지 않았다면
        if not visited[i]:
            # DFS 처리
            DFS(i)


# 노드 선언
for _ in range(m):
    s, e = map(int, input().split())
    # 양방향 에지이므로 양쪽에 에지를 더함
    A[s].append(e)
    A[e].append(s)

# DFS 횟수를 세기 위한 변수
count = 0

for i in range(1, n + 1):
    # 연결 노드 중 방문하지 않은 노드만 탐색
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
