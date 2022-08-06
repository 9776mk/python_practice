chess_ = [1,1,2,2,2,8]
piece_ = list(map(int, input().split()))
right_set = []

for i in range(6):
    right_set.append(chess_[i] - piece_[i])

for num in right_set:
    print(num, end=' ')
