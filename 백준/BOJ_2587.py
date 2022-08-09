list_ = []

for _ in range(5):
    list_.append(int(input()))

list_.sort()

print(int(sum(list_)/5))
print(list_[2])