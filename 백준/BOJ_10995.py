N = int(input())

if N == 1:
    print('* ')
else:
    for i in range(1,N+1):
        for j in range(1,N+1):
            # 홀수번째 줄일 때(1,3,5)
            if i%2 !=0:
                print('* ', end='')
            # 짝수번째 줄이면
            else:
                print(' *', end='')
        print('')