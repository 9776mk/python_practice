N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
mid_num = N//2

print(num_list[mid_num])
