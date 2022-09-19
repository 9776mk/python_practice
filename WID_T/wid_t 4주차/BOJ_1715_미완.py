from collections import deque

N = int(input())

list_ = []

for i in range(N):
    list_.append(int(input()))

list_.sort()

deque_ = deque(list_)


sum_ = 0

while deque_:
    for i in range(2):
        sum_ += deque.popleft()

print(sum_)