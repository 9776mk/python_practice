# from collections import deque


# def bfs(n):
#     queue = deque()
#     queue.append(n)

#     while queue:
#         # 100에 도달한 경우 바로 while문 종료
#         n = queue.popleft()

#         if n in dict_.keys():
#             if list_[dict_[n]] == 0:
#                 # 사다리/뱀을 통해 내려간 곳은 주사위 횟수없이 바로 추가
#                 list_[dict_[n]] = list_[n]
#                 queue.append(dict_[n])
#         # n의 값이 사다리 / 뱀 리스트에 없는 경우
#         else:
#             for i in range(1, 7):
#                 # 범위 안에 있고
#                 if n + i <= 100:
#                     # 방문하지 않았다면
#                     if list_[n + i] == 0 or list_[n + i] > list_[n] + 1:
#                         list_[n + i] = list_[n] + 1
#                         queue.append(n + i)

#     return list_[100]


# list_ = [0] * 101
# dict_ = {}

# x, y = map(int, input().split())

# for i in range(x + y):
#     a, b = map(int, input().split())
#     dict_[a] = b

# print(bfs(1))

from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        n = queue.popleft()
        for i in range(1, 7):
            new = n + i
            if 0 < new <= 100 and not visited[new]:
                if new in dict_.keys():
                    new = dict_[new]

                if not visited[new]:
                    queue.append(new)
                    visited[new] = True
                    board_[new] = board_[n] + 1


N, M = map(int, input().split())
board_ = [0] * 101
visited = [False] * 101

dict_ = {}

for i in range(N + M):
    a, b = map(int, input().split())
    dict_[a] = b

bfs(1)
print(board_[100])
