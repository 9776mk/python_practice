from pprint import pprint

T = int(input())

for _ in range(T):
    m, n = map(int, input().split())
    matrix_ = []
    matrix_ = [list(map(int, input().split())) for _ in range(m)]

#    pprint(matrix_)

    transed_matrix = [[0] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            transed_matrix[r][c] = matrix_[c][r]

#    pprint(transed_matrix)
    # 첫 번째 1은 인덱스 0에, 두 번째 1은 인덱스 1로, ... n번째 1은 인덱스 n-1로 이동해야 한다.
    # 만약 1이라면 그 1이 몇 번째인지를 이용해 해당 인덱스와의 차이를 구하면 된다.
    sum_ = 0
    
    for i in range(n):
    # i행에 1이 몇 개 인지 셈
        cnt_1 = transed_matrix[i].count(1)
        for j in range(m):
        # 3 번째 1(cnt_1 = 3)은 인덱스상 m-3에 있어야 함. 따라서 이동할 거리는 m - 3 - 현재 위치의 인덱스
        # 2 번째 1(cnt_1 = 2)은 인덱스상 m-2에 있어야 함. 따라서 이동할 거리는 m - 2 - 현재 위치의 인덱스
        
            if transed_matrix[i][j] == 1:
                go_idx = m - cnt_1
                sum_ += go_idx - j
                cnt_1 -= 1

    print(sum_)