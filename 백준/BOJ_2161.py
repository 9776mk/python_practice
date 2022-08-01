from collections import deque

n = int(input())
list_n = []
card_list = []
list_n = deque(list_n)

# 1 ~ n부터까지의 리스트 생성
for i in range(1,n+1):
    list_n.append(i)

# n-1까지 진행
for i in range(n):
    # n - 1이 아닐 때, pop이 가능할 때
    if i != n-1:
        card_list.append(list_n.popleft())
        list_n.append(list_n.popleft())
    # list_n의 마지막 원소일 때
    else:
        card_list.append(list_n.popleft())
# 하나씩 출력
for num in card_list:
    print(num, end=' ')

''' 
# 간단히 표현
from collections import deque

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    print(queue.popleft(), end=' ')
    queue.append(queue.popleft())

print(queue[0])
'''