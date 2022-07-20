T = int(input())

for test_case in range(1,T+1):
    P,Q,R,S,W = map(int, input().split())

    cost_A = W * P
    if W <= R:
        cost_B = Q
    else:
        cost_B = Q + (W-R)*S
    
    cost = min(cost_A, cost_B)
    print(f'#{test_case} {cost}')

    # print(f'#{test_case} {cost_A}' if cost_A < cost_B else f'#{test_case} {cost_B}')