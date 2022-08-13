T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    list_ = list(map(int, input().split()))
    list_.sort()
    
    print(f'#{test_case}', end=' ')
    for i in list_:
        print(i, end=' ')
    print()