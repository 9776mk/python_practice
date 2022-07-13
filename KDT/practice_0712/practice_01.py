#주어진 n이 3의 배수이면서 짝수인 경우 '참' 거짓인 경우 '거짓' 출력

n = 14

if n % 3 != 0:
    print('거짓')

else:
    if n%2 ==0:
        print('참')
    else:
        print('거짓')