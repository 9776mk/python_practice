n, m = map(int, input().split())

list_ = list(map(int, input().split()))

max_ = 0

# 시간 초과
# for i in range(n-m+1):
#     sum_ = 0
#     for j in range(m):
#         sum_ += list_[i+j]
#     if sum_ > max_:
#         max_ = sum_

# 제일 처음 구간의 합을 구함
sum_list = []
sum_1 = 0
for i in range(m):
    sum_1 += list_[i]
sum_list.append(sum_1)

sum_temp = sum_1
for i in range(n-m):
    sum_temp -= list_[i]
    sum_temp += list_[i+m]
    sum_list.append(sum_temp)

print(max(sum_list))