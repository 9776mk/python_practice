# T = int(input())

# for tc in range(1, T+1):
#     # N: 사람수, M초의 시간을 들이면 K개의 붕어 만들수있음
#     N, M, K = map(int, input().split())
#     arrive_time = list(map(int, input().split()))
#     arrive_time.sort()

#     result = "Possible"
#     # x초까지 만들어진 붕어 개수: (x // M) * K
#     for i in range(N):
#         boong = (arrive_time[i] // M) * K - (i+1)
#         if boong < 0:
#             result = "Impossible"
#             break
#     print(f'{tc} {result}')


T = int(input())

for tc in range(1, T+1):
    # N: 사람수, M초의 시간을 들이면 K개의 붕어 만들수있음
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time.sort()

    result = "Possible"
    # x초까지 만들어진 붕어 개수: (x // M) * K
    for i in range(N):
        boong = (arrive_time[i] // M) * K - (i+1)
        if boong < 0:
            result = "Impossible"
            break

    print(f'#{tc} {result}')