# 가지고 있는 카드
N = int(input())
list_N = list(map(int, input().split()))
list_N.sort()

# 확인용 카드
M = int(input())
list_M = list(map(int, input().split()))

# 이진 탐색
for i in range(M):
    find = False

    target = list_M[i]
    start = 0
    end = N-1

    # 왼쪽 포인터가 오른쪽 포인터보다 작을때 반복
    while start<=end:
        mid_i = int((start+end)/2)
        mid_value = list_N[mid_i]

        if mid_value > target:
            end = mid_i - 1
        elif mid_value < target:
            start = mid_i + 1
        else:
            find = True
            break

    if find:
        print(1, end=" ")
    else:
        print(0, end=" ")