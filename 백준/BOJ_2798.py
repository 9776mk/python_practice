N, M = map(int, input().split())
list_ = list(map(int, input().split()))

sum_ = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_tmp = 0
            sum_tmp = list_[i] + list_[j] + list_[k]
            if sum_ < sum_tmp < M:
                sum_ = sum_tmp
            elif sum_tmp == M:
                sum_ = sum_tmp
                break
        if sum_ == M:
            break
    if sum_ == M:
            break

print(sum_)