A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result = str(result)

num_dict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for num in result:
    if num in num_dict.keys():
        num_dict[num] += 1

for num in num_dict:
    print(num_dict[num])
