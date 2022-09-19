N = int(input())

list_ = []

for i in range(N):
    list_.append(int(input()))

list_.sort(reverse=True)

sum_ = 0

while len(list_) != 1:
    for _ in range(2):
        sum_ += list_.pop()

    list_.append(sum_)
    list_.sort()
    
    if len(list_) == 1:
        sum_ += list_.pop()

print(sum_)