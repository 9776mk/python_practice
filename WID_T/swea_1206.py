import sys
sys.stdin = open('swea_1206.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))

    # 현재 값 인덱스 i를 기준으로, i-2, i-1, i+1, i+2를 비교한 후 i가 제일 크다면, i 다음으로 큰 값과의 차이만큼이 조망권이 확보된 세대
    # 0 이면 넘어감
    # 양쪽 끝에 0이 두 개씩 주어지므로, 계속 할 수 있음.

    # 조망권이 확보된 세대의 수
    # 조망권 : right of view
    rov = 0

    # 2번째로 높은 높이
    height_2 = 0

    len_ = len(height)

    for i in range(2,len_-2):
        # 0이면 비교하지 않고 계속 진행
        if height[i] == 0:
            continue
        
        else:
            if height[i] == max(height[i-2], height[i-1], height[i], height[i+1], height[i+2]):
                height_2 = max(height[i-2], height[i-1], height[i+1], height[i+2])
                
                rov += height[i] - height_2
    print(f'#{test_case} {rov}')