N, M = map(int, input().split())

matrix_ = [list(map(int, input().split())) for _ in range(N)]

# print(matrix_)

K = int(input())

for i in range(K):
    sum_ = 0
    i, j, x, y = map(int, input().split())
    # 입력 받은 값과 
    i, j, x, y = i-1, j-1, x-1, y-1

    # i == x, j == y -> matrix[i][j] 출력
    if i == x and j == y:
        print(matrix_[i][j])

    # j == y가 같으면, (i,j) + (i+1,j) + ... + (x-1, y) + (x,y) 출력
    elif i != x and j == y:
        for a in range(i, x+1):
            sum_ += matrix_[a][y]
        
        print(sum_)
    # i !=x , j != y -> (i,j) ~ (i,y) + (x,j) ~ (x,y)
    else:
        for a in range(i, x+1):
            for b in range(j, y+1):
                sum_ += matrix_[a][b]

        print(sum_)