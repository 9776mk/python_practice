# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

numbers = [0, 20, 100] 
#numbers = [0, 20, 100, 50, -60, 50, 100] # 50
#numbers = [0, 1, 0] # 0
# numbers = [-10, -100, -30] # -30

min_num = numbers[0]
for n in numbers:
    if (min_num >= n):
        min_num = n
    else:
        continue
max_num_1 = min_num
max_num_2 = min_num

# max_num을 설정
for i in numbers:
    if max_num_1 <= i:
        max_num_1 = i
    else:
        continue

for j in numbers:
    if j != max_num_1:
        if max_num_2 < j:
            max_num_2 = j
        else:
            continue
    continue

print(max_num_2)