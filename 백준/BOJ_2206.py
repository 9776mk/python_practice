N, M = map(int, input().split())

list_ = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

print(list_)
print(visited)
