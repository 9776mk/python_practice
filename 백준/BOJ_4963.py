# from pprint import pprint


# def is_island(list_):
#     stack = list_[0][0]
#     visited = [[False] * w for _ in range(h)]









# while True:
#     w, h = map(int, input().split())

#     visited = [[False] * w for _ in range(h+1)]

#     # 0,0 이라면 종료
#     if w == 0 and h == 0:
#         break
#     # 0,0 이 아니라면
#     else:
#         map_ = []
#         # 2차원 배열로 입력받음
#         for i in range(h):
#             a = list(map(int, input().split()))
#             map_.append(a)
#         pprint(map_)

w = 3
h = 2
visited = [[False] * w for _ in range(h)]

print(visited)