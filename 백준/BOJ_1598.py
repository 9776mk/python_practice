# a,b 숫자를 입력 받음
a, b = map(int, input().split())

# 숫자의 좌표는 (n%4-1, n//4)로 정해짐
def dot(n):
    # n이 4의 배수이면
    # (3, 0), (3, 1). (3, 2)
    if n%4 == 0:
        return 3, int(n/4)-1
    # n이 4의 배수가 아니면
    # 1 : (0,0), 11 :(2,2)
    else:
        x = n%4
        y = n//4
        return x-1,y

# 직각거리 = x좌표 차 + y좌표 차
print(abs(dot(a)[0] - dot(b)[0]) + abs(dot(a)[1] - dot(b)[1]))