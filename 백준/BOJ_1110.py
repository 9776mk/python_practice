N = str(input())
first_N = int(N)
comp_N = None


if int(N) < 10:
    N = '0' + N

cnt = 0

while comp_N != first_N:
    new_N = int(N[0]) + int(N[1])
    new_N = str(new_N)
    if int(new_N) < 10:
        new_N = '0' + new_N
    N = N[1] + new_N[1]
    comp_N = int(N)
    cnt += 1

print(cnt)
