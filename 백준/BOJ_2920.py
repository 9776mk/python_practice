N = list(map(int, input().split()))

ascending_list = [1,2,3,4,5,6,7,8]
descending_list = [8,7,6,5,4,3,2,1]

result = ''

if N == ascending_list:
    print('ascending')
elif N == descending_list:
    print('descending')
else:
    print('mixed')