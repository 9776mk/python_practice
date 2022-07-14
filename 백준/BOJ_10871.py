N, X = map(int, input().split())
list_A = list(map(int, input().split()))
new_list = []

for num in list_A :
    if num < X:
        new_list.append(num)
    else:
        continue

for i in new_list:
    print(i, end=' ')