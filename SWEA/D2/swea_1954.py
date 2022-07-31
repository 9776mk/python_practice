#T = int(input())
T = 1

for test_case in range(1, T+1):
    #N = 3
    N = int(input())

    snail_ =  [[0 for col in range(N)] for row in range(N)]

    #print(snail_)

    a = 0
    number_ = 1

    while number_ <= N*N:

        # 가로 [0][0] ~ [0][n-1] 1 ~ n (n번)
        for i in range(N):
            if number_ > N * N:
                break 
            snail_[a][a+i] = number_
            number_ += 1


        # 세로 [1][n] ~ [n-1][n-1] n ~ 2n-1 까지 (n-1번)
        for j in range(1,N):
            if number_ > N * N:
                break
            snail_[j][N-1] = number_
            number_ += 1

        # 가로 [n-1][n-2] ~ [n-1][0] 2n ~ 3n -2 까지 (n-1번) #거꾸로
        for k in range(2, N+1): 
            if number_ > N * N:
                break
            snail_[N-1][N-k] = number_
            number_ += 1

        # 세로 [n-2][0] ~ [n+2][0] 3n-1 부터 4n-3까지 (n-2번) #거꾸로
        for l in range(2,N):
            if number_ > N * N:
                break  
            snail_[N-l][0] = number_
            number_ += 1

        a += 1
            
        
    print(snail_)

for i in range(N):
    for j in range(N):
        print(snail_[i][j], end= ' ')
    print()    