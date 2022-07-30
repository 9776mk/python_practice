# 생성자를 만드는 함수를 정의
def saengsungja(num):
    saengsungja_num = num
    while num !=0:
        saengsungja_num += num%10
        num //= 10
    return saengsungja_num

selfnum_list = []

# 1부터 10000까지 중
for i in list(range(1, 10001)):
    # 1~10000까지 생성자를 만들고 
    selfnum_list.append(saengsungja(i))
    # 만약 i가 생성자 리스트 안에 없으면 == self_number
    if i not in selfnum_list:
        print(i)














# # 생성자인지 검사를 하고, 생성자가 없으면 추가 -> O(N^2)? 이 걸리는 것 같다.
# self_num_list = []

# for i in range(1, 10001):
#     n = i
#     is_solo = True

#     while n != 0:
#         n -= 1
#         tmp_sum = 0

#         for num in str(n):
#             tmp_sum += int(num)
        
#         if n + tmp_sum == i:
#             is_solo = False
#             n == 0
#             break
#         else: 
#             continue

#     if is_solo == True:
#         self_num_list.append(i)
#     else:
#         continue

# for num in self_num_list:
#     print(num)