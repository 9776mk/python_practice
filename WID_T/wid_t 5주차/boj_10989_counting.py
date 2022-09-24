N = int(input())
list_ = []

for i in range(N):
    list_.append(int(input()))

count = [0] * (max(list_) + 1)

for num in list_:
    count[num] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * (len(list_))

for num in list_:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1

for i in result:
    print(i)