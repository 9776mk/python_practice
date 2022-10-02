import sys
input = sys.stdin.readline

# 사용자 입력 받기
N, M = map(int, input().split())
list_ = list(map(int, input().split()))

# 구간 합 리스트 구하기
sum_list = [0]
sum_ = 0
for i in range(N):
    sum_ += list_[i]
    sum_list.append(sum_)

#print(sum_list)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])