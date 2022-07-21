# 3, 6, 9가 들어갈 때마다 -를 출력
# 33, 36, 39 같이 여러개가 들어가면 그 갯수만큼 --를 출력해야함.

N = int(input()) #N을 입력받음

for number in range(1, N+1): # 1~N 까지의 범위에서
    str_number = str(number) # number를 활용하기 위해 str로 바꿈
    cnt = 0
    # 만약 number 안에 3 or 6 or 9가 있다면
    if ('3' in str_number) or ('6' in str_number) or ('9' in str_number): # count()가 있는 것의 숫자만 세어주기 때문에 이 조건문은 없어도 된다. 대신 print문에 cnt를 활용해야한다.
        cnt += str_number.count('3') + str_number.count('6') +str_number.count('9')
        print('-'*cnt, end=' ') 
    else:
        print(str_number, end=' ')



'''
# 3, 6, 9가 들어갈 때마다 -를 출력
# 33, 36, 39 같이 여러개가 들어가면 그 갯수만큼 --를 출력해야함.
N = int(input()) #N을 입력받음

list_369 = ['3','6','9'] # 3,6,9 리스트를 만듦

for number in range(1, N+1): # 1~N 까지의 범위에서
    cnt = 0 # cnt = 0
    for j in str(number): # number라는 글자 안에
        if j in list_369: #3,6,9가 들어 있을 때마다
            cnt+= 1 # cnt에 1씩 더 해준다.
    if cnt > 0: # 만약 cnt가 0이 아니라면, 즉 3,6,9가 적어도 하나는 들어있으면
        number = '-' * cnt # number에 cnt 횟수만큼 '-'를 곱해준다.
    print(number, end=' ') #그리고 number를 출력한다.
'''