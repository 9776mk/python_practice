import heapq

N = int(input())

list_n = []

# 입력받은 숫자들을 리스트에 저장
for _ in range(N):
    list_n.append(int(input()))

# heap을 위해 heapfi를 진행
heapq.heapify(list_n)

# heappop으로 하나씩 출력하면 최솟값들이 출력
for _ in range(N):
    print(heapq.heappop(list_n))
