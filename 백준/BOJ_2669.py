from pprint import pprint

list_ = [[0] * 100 for _ in range(100)]


for i in range(4):
    cnt_ = 0
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1-1, x2-1):
        for j in range(y1-1, y2-1):
            list_[i][j] = 1

    for i in range(10):
        for j in range(10):
            if list_[i][j] == 1:
                cnt_ += 1
print(cnt_)

# from pprint import pprint

# list_ = []

# max_x, max_y = 0, 0

# # 좌표계 생성
# for i in range(4):
#     list_.append(list(map(int, input().split())))

# for i in range(4):
#     if list_[i][2] > max_x:
#         max_x = list_[i][2]

# for i in range(4):
#     if list_[i][3] > max_y:
#         max_y = list_[i][3]

# matrix_ = [[0] * max_x for _ in range(max_y)]

# # 입력 
# # 1,2,4,4, -> 0,1,2,2
# # 2,3,5,7 -> 1,2,3,5


# for i in range(4):
#     for j in range(list_[i])
