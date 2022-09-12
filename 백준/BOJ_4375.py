# # n 입력 받음
# while True:
#     try:
#         n = int(input())
#     except:
#         break
    
#     while True:
#         multiple = '1'
#         if int(multiple) % n == 0:
#             print(len(multiple))
#             break
#         else:
#             multiple = multiple + '1'

while True:
    multiple = '1'
    n = int(input())

    while True:
        if int(multiple) % n == 0:
            print(len(multiple))
            break
        else:
            multiple = multiple + '1'