N = int(input())

list_ = []
dict_ = {}

for i in range(5):
    list_.append(int(input()))

for i in range(N):
    dict_[list_[i]] = dict_.get(list_[i], 0) + 1

for k, v in dict_.items():
    count_ = 0
    max_v = 0
    max_2 = 0
    for i in dict_.values():
        if i > max_v:
            max_v = i
        elif max_v > i > max_2:
            max_2 = i

    if v == max_v:
        count_ += 1

    if count_ == 1:
        print(k)
    else:
        print(k)
