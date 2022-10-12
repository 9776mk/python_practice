import sys
input = sys.stdin.readline


M, n = map(int, input().split())
dir_ = 1000

list_ = []
a, b = 0, 0

for _ in range(n):
    list_.append(list(map(str, input().split())))
    #print(list_)

for i in range(n):
    if list_[i][0] == 'MOVE': 
        # 0이면 
        # 오른쪽 방향
        if dir_ % 4 == 0:
            a += int(list_[i][1])
            print(a, b)
        # 위쪽 방향
        elif dir_ % 4 == 1:
            b += int(list_[i][1])
            print(a, b)
        # 왼쪽 방향
        elif dir_ % 4 == 2:
            a -= int(list_[i][1])
            print(a, b)
        # 아래쪽 방향
        elif dir_ % 4 == 3:
            b -= int(list_[i][1])
            print(a, b)

    elif list_[i][0] == 'TURN':
        # 0이면 반시계 90도로 돌리기
        if list_[i][0]:
            dir_ += 1
        # 1이면 시계 90도 돌리기
        elif list_[i][1]:
            dir_ -= 1

if a < 0 or b < 0 or a > M or b < M:
    print(-1)
else:
    print(a, b)


'''
import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, n = map(int, input().split())
x, y = 0, 0
dir = 0
check = False
for _ in range(n):
    com, num = map(str, input().rstrip().split())

    if com == "TURN":
        if num == "1":
            dir -= 1
            if dir < 0:
                dir = 3
        else:
            dir += 1
            if dir > 3:
                dir = 0
    elif com == "MOVE":
        x += int(num) * dx[dir]
        y += int(num) * dy[dir]
        if x < 0 or x >= M or y < 0 or y >= M:
            print(-1)
            check = True
            break
if not check:
    print(y, x)
'''