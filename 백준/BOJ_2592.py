list_ = []

freq_std = 0
freq_num = 0

for _ in range(10):
    list_.append(int(input()))

for number in list_:
    cnt_num = list_.count(number)
    if cnt_num >= freq_std:
        freq_std = cnt_num
        freq_num = number

print(int(sum(list_)/10))
print(freq_num)