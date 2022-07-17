num_list = []

for i in range(9):
    a = int(input())
    num_list.append(a)

#print(num_list)

max_num = max(num_list)
max_ind = num_list.index(max_num)

print(max_num)
print(max_ind+1)