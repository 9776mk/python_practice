import heapq
import sys

input = sys.stdin.readline

N = int(input())

list_ = []
heapq.heapify(list_)


for _ in range(N):
    x = int(input())

    # x가 0이 아니면
    if x != 0:
        heapq.heappush(list_, x)
    # x가 0이면
    else:
        if len(list_) == 0:
            print(0)
        else:
            print(heapq.heappop(list_))