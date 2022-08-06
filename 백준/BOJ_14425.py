N, M = map(int, input().split())
set_n = set()
list_m = []
cnt = 0

for _ in range(N):
    set_n.add(input())

for _ in range(M):
    list_m.append(input())

# print(len(set_n & set_m))

for elem_m in list_m:
    if elem_m in set_n:
        cnt += 1

print(cnt)