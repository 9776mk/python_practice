# w로 시작하는 것과, b로 시작하는 것을 구함
w_start = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
b_start = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

# 판을 입력받음

M, N = map(int, input().split())
board= []
for _ in range(M):
   board.append(list(map(str, input())))

#print(board)

# 최솟값을 구하기 위해 큰 수를 입력
min_w_cnt = 100
min_b_cnt = 100

# M, N 체스판을 돌기 위한 범위 설정 0 ~ M-8+1과 0 ~ N-8+1
for i in range(0, M-8+1):
    for j in range(0, N-8+1):
        w_cnt = 0
        b_cnt = 0
        # w_start와 b_start와 비교하기 위한 for문
        for k in range(0, 8):
            for l in range(0, 8):
                # 흰색 시작판과 비교
                if w_start[k][l] == board[i+k][j+l]:
                    w_cnt += 0
                else:
                    w_cnt += 1
                # 검은색 시작판과 비교
                if b_start[k][l] == board[i+k][j+l]:
                    b_cnt += 0
                else:
                    b_cnt += 1
        # 현재 저장된 최솟값과 새로운 최솟값 중 더 작은 값을 넣음
        if w_cnt < min_w_cnt:
            min_w_cnt = w_cnt
        if b_cnt < min_b_cnt:
            min_b_cnt = b_cnt

# 둘 중 더 작은 값 출력
print(min(min_w_cnt, min_b_cnt))