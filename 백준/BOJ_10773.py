K = int(input())

list_ = []

for _ in range(K):
    n = int(input())

    if n != 0:
        list_.append(n)
    else:
        list_.pop()

print(sum(list_))