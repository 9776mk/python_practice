# import sys
# input = sys.stdin.readline

# N = int(input())

# name_dict = {}

# for _ in range(N):
#     name_ = input()
#     if name_ in name_dict:
#         name_dict[name_] += 1
#     else:
#         name_dict[name_] = 1

# for _ in range(N-1):
#     name_ = input()
#     if name_ in name_dict:
#         name_dict[name_] -= 1

# for name in name_dict:
#     if name_dict[name] != 0:
#         print(name)

import sys
input = sys.stdin.readline

N = int(input())

name_dict = {}

full_name = ''

for _ in range(N):
    name_ = input()
    name_dict[name_] = name_dict.get(name_, 0) + 1

for _ in range(N-1):
    name_ = input()
    name_dict[name_] -= 1

for k, v in name_dict.items():
    if v != 0:
        full_name = k

print(full_name)