from collections import deque
import collections

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    list_ = list(map(int, input().split()))

    # list를 deque으로 바꾸는 방법
    deque_ = collections.deque(list_)

    for _ in range(M):
        deque_.append(deque_.popleft())

    print(f'#{test_case} {deque_.popleft()}')