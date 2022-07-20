# 1대 1 가위바위보
# 가위 1 바위 2 보 3
# A가 이기는 경우 : 1 3 / 2 1 / 3 2
# B가 이기는 경우 : 3 1 / 1 2 / 2 3


A, B = map(int, input().split())

if (A==1 and B==3) or (A==2 and B==1) or (A==3 and B==2):
    print('A')
else:
    print('B')