T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    
    n_max = n_list[0]
    n_min = n_list[0]
    
    for i in range(0, N):
        if (n_list[i]>n_max):
            n_max = n_list[i]
        elif(n_list[i]<n_min):
            n_min = n_list[i]

    print(f'#{test_case} {n_max-n_min}')