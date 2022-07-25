T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    
    profit = 0
    max_price = 0
    min_index = 0
    max_index = 0

    while True:
        for i in range(min_index, N):
            if max_price < price[i]:
                max_price = price[i]
                max_index = i

        for j in range(min_index, max_index):
            profit += (max_price - price[j])
        
        max_price = 0
        min_index = max_index+1


        if min_index == N:
            print(f'#{test_case} {profit}')
            break