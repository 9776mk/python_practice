N = 5
list_ = [['.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['.', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']]
'''
N = int(input())
list_ = []
for _ in range(N):
    list_.append(list(input()))
'''

garo_ = 0
garo_space = []
sero_ = 0
sero_space = []

for i in range(N):
    for j in range(N):
        if j == N-1 and list_[i][j]=='.':
            garo_space.append('x')
            if len(garo_space) >= 2:
                garo_ += 1
            garo_space.clear()
            break

        # 만약 .이면
        elif list_[i][j] == '.':
            # 가로에 . 추가
            garo_space.append('.')
        # 만약 X라면
        elif list_[i][j] == 'X':
            # garo_space의 길이가 2 이상일 경우
            if len(garo_space) >= 2:
                # garo_에 +1 
                garo_ += 1
            # 누적되지 않게 초기화
            garo_space.clear()

for i in range(N):
    for j in range(N):
        if j == N-1 and list_[j][i]=='.':
            sero_space.append('x')
            if len(sero_space) >= 2:
                sero_ += 1
            sero_space.clear()
            break

        # 만약 .이면
        if list_[j][i] == '.':
            # 세로에 . 추가
            sero_space.append('.')
        # 만약 X라면
        elif list_[j][i] == 'X':
            # sero_space 길이가 2 이상일 경우
            if len(sero_space) >= 2:
                # sero_에 +1 
                sero_ += 1
            # 누적되지 않게 초기화
            sero_space.clear()

print(garo_, sero_)