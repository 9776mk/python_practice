N, M = map(int, input().split())

# 2차원 리스트에 입력을 저장
castle_ = [list(input()) for _ in range(N)]
castle_row = []

# 행과 열의 정보를 담을 리스트 선언
list_guard = []

cnt_no_row = 0
cnt_no_col = 0

# 경비가 없는 행의 수를 셈
for i in range(N):
    if 'X' not in castle_[i]:
        cnt_no_row += 1    
# 경비가 없는 열의 리스트를 만들고
for j in range(M):
    for k in range(N):
        if castle_[k][j] != 'X':
            list_guard.append(k)
        
    if len(list_guard) == N:
        cnt_no_col += 1

    list_guard = []
        # X가 하나라도 있으면
        # 가드가 필요없으니까
        # X가 하나도 없으면
        # cnt_no_col += 1

print(max(cnt_no_row, cnt_no_col))