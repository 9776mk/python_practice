# # # 교과서 수 N, 교과서 더미의 수 M
# N, M = map(int, input().split())

# ki_list = []

# num_list = list(range(1,N+1))

# # # 2차원 list로 입력받기
# # # [[3, 1], [4, 2]]
# for _ in range(M):
#     ki = int(input())
#     ki_list.append(list(map(int, input().split())))

# # print(ki_list)
# N = int(input())

# # idx_list = list(range(1,N+1))

# # print(idx_list)

# # pop값의 크기 비교
# # for i in range(M):




# n,m = map(int, input().split())

# list_2 = []

# for i in range(m):
#     a = int(input())
#     list_number = list(map(int,input().split()))

#     for j in range(0,len(list_number)-1):
#         if list_number[j] < list_number[j+1]:
#             list_2.append(list_number[j+1])
        
            
# if list_2 == []:
#     print('Yes')
# else:
#     print('No')

num_list = list(range(1,10))

print(num_list)