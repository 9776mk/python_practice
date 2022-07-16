N = input()
n_first = N
temp_n = 0
cnt = 0
n_is_equal = False


while n_is_equal != True:
    if len(N) == 1: #N이 한 글자인 경우
        N = '0' + N
        cnt += 1
        if N == n_first:
            n_is_equal = True
            break

        else:
            continue
    
    else: # len(N) ==2, 2글자
        temp_n = str(int(N[0]) + int(N[1]))
        cnt += 1
        if len(temp_n) == 1:
            temp_n = '0' + temp_n
            N = N[1] + temp_n[1]
            if N == n_first:
                n_is_equal = True
                break
            else:
                continue
        else: # 2글자 이면
            N = N[1] + temp_n[1]
            if N == n_first:
                n_is_equal = True
                break
            else:
                continue

print(cnt)