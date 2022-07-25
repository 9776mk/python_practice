N = int(input())
old_N = N
cnt = 0
is_True = True

while is_True:
    cnt += 1
    N = (N % 10)*10 + ((N//10 + N%10)%10)

    if N == old_N:
        is_True = False

print(cnt)