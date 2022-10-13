n = int(input())

list_ = []
for _ in range(n):
    list_.append(list(map(int, input().split())))

print(list_)