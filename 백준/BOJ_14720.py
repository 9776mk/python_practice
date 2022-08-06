# 우유 가게 수 N 입력
N = int(input())

# 우유 가게 정보 입력
store_ = list(map(int, input().split()))

cnt = 0
tmp = 0

for i in range(0,N):
    # 0이 처음 나올 때 무조건 +1 해주기
    if tmp == 0 and store_[i] == 0:
        cnt += 1
        tmp = 1
    # 0 다음 1이 나올 때 +1
    elif tmp == 1 and store_[i] == 1:
        cnt += 1
        tmp = 2
    # 1 다음 2 나올 때 +1
    elif tmp == 2 and store_[i] == 2:
        cnt += 1
        tmp = 3
    # 2 다음 0 나올 때 +1
    elif tmp == 3 and store_[i] == 0:
        cnt += 1
        tmp = 1

print(cnt)