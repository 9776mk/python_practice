N = int(input())

# N이 99이하인 경우 무조건 한수
if N <=99:
    print(N)
# N이 네 자릿수인 경우는 1000밖에 없으므로 따로 지정 / 999와 같으므로 N=999로 다시 지정해도 됨
elif N == 1000:
    print(144)

# 만약 세 자릿수인 경우(100~999)    
else:
    # 1~99까지의 값인 99를 cnt의 기본값으로 할당하고
    cnt = 99
    for number in range(100,N+1):
        number = str(number)
        # 절댓값으로 하는 경우 101의 경우 등차수열로 인정되므로 각 자릿수끼리 계산
        if int(number[0])-int(number[1]) == int(number[1])-int(number[2]):
            cnt += 1
        else:
            continue
    print(cnt)