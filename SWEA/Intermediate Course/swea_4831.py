# 전기 버스
# T = int(input())

# for test_case in range(1, T+1):
#   # 최대거리 K, 목표 정류장 N, 충전기 M
#    K, N, M = map(int, input().split())
#    bus_stop = list(map(int, input().split()))

K, N, M = 3, 10, 5
bus_stop = [1,3,5,7,9]

# 충전 횟수 설정
charge = 0

# 현재의 정류장 변수
# 0부터 시작
tmp = 0

for i in range(M):
    # 만약 두 정류장 사이의 거리가 K보다 짧다면
    if bus_stop[i] - bus_stop[tmp] < K:
        # 계속 진행
        continue
    # 만약 두 정류장 사이의 거리가 K보다 멀다면
    # 즉, 도달할 수 없으면
    elif bus_stop[i] - bus_stop[tmp] > K
        if tmp != i-1:
            tmp = i-1
            # 충전 횟수 +1
            charge += 1

    