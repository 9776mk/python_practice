# 숫자가 있으면
# 그 숫자를 만드는 생성자가 있는지 검사를 하고

# 있으면 넘어가고, 없으면 셀프 넘버에 추가
self_num_list = []

for i in range(1, 10001):
    n = i
    is_solo = True

    while n != 0:
        n -= 1
        tmp_sum = 0

        for num in str(n):
            tmp_sum += int(num)
        
        if n + tmp_sum == i:
            is_solo = False
            n == 0
            break

        else: 
            continue

    if is_solo == True:
        self_num_list.append(i)
    else:
        continue

for num in self_num_list:
    print(num)