n = int(input())

# 점수에 따라 A~F까지 출력
if 100 >= n >= 90:
    print('A')
elif n >= 80:
    print('B')
elif n >= 70:
    print('C')
elif n >= 60:
    print('D')
else:
    print('F')