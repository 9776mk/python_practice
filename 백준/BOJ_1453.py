N = int(input())

list_ = list(map(int, input().split()))
dict_ = {}

for elem in list_:
    dict_[elem] = dict_.get(elem, 0) + 1

sum_ = 0

for v in dict_.values():
    if v != 1:
        sum_ += v - 1

print(sum_)