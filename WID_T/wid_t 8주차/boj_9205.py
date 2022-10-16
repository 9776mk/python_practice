from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    list_ = []
    for _ in range(n+2):
        list_.append(list(map(int, input().split())))
    print(list_)