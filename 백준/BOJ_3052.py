num_list = []
remain_list = []

for i in range(10):
    N = int(input())
    num_list.append(N)

#print(num_list)

for num in num_list:
    remain_list.append(num%42)

remain_list = set(remain_list)

print(len(remain_list))