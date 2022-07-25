x = int(input())
y = int(input())


# x, y 숫자가 양,음수냐에 따라 사분면 출력
if x > 0 and y > 0 :
    print('1')
elif x < 0 and y > 0 :
    print('2')
elif x < 0 and y < 0 :
    print('3')
else:
    print('4')