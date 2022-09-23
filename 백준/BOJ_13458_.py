N = int(input())
list_A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in list_A:
    num = i - B
    cnt += 1

    # 남은 사람이 0명이상일 때
    if num > 0:
        # 남은 사람이 C명 보다 적을 경우
        if num <= C:
            cnt += 1
        # 남은 사람이 C명보다 많지만
        else:
            # 나눠떨어지면
            if num % C == 0 :
                cnt += num // C
            # 안 나눠떨어지면
            else:
                cnt += (num // C) + 1
print(cnt)