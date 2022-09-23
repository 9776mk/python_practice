N, K = map(int, input().split())

list_ = []

for i in range(N):
    list_.append(int(input()))

list_.sort(reverse=True)
#print(list_)

cnt = 0

for i in range(N):
    if list_[i] <= K:
        cnt += K // list_[i]
        K = K % list_[i]
print(cnt)