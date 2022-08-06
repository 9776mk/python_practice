chess_ = [list(input()) for _ in range(8)]

print(chess_)

cnt = 0

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0 and chess_[i][j] == 'F':
            cnt += 1
        else:
            continue

print(cnt)