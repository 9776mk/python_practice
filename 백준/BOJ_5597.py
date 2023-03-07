list_ = []
not_in = []

for i in range(28):
    list_.append(int(input()))

for j in range(1, 31):
    if j not in list_:
        not_in.append(j)
    else:
        continue

not_in.sort()

for k in range(2):
    print(not_in[k])