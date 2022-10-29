def monotonic(N):
    N = str(N)
    if len(N) <=1:
        return False

    is_mono = True
    tmp = 1
    for i in N:
        if tmp <= int(i):
            tmp = int(i)
        else:
            is_mono = False
            break
    return is_mono

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list_ = list(map(int, input().split()))
    list_.sort(reverse=True)

    is_monotonic = False

    for i in range(N-1):
        for j in range(i+1, N):
            result = list_[i] * list_[j]
            
            is_monotonic = monotonic(result)

            if is_monotonic:
                break
            else:
                continue

        if is_monotonic:
            break

    if is_monotonic:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')