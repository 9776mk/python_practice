# N = int(input())

# num_dict = {}

# for _ in range(N):
#     input_ = input()
#     num_dict[input_] = num_dict.get(input_, 0) +1

# max_val = -float('inf')
# max_key = float('inf')

# for k, v in num_dict.items():
#     if v > max_val:        
#         max_val = v
#         max_key = k
#     else:
#         continue

# print(max_key)

N = int(input())

num_dict = {}

for _ in range(N):
    input_ = int(input())
    num_dict[input_] = num_dict.get(input_, 0) +1

max_val = -2**(64)
min_key = 2**(64)


# k, v 끼리 비교
# v 값이 큰 k 값을 찾아야함.
# 만약 v 값이 같다면 더 작은 k 값

for k, v in num_dict.items():
    if v > max_val:
        max_val = v
        min_key = k
    
    elif v == max_val:
        if min_key > k:
            min_key = k            
    else:
        continue

print(int(min_key))