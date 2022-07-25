T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    max_M = 0
    min_M = 0
    sum = 0


    list_N = list(map(int, input().split()))

    for i in range(N-M+1):
        for j in range(M):

