N = input()

goldmin = ['4','7']
silvermin = ['1','2','3','5','6','8','9','0']

while True:
    new_n = ''
    for digit in N:
        if digit in goldmin and digit not in silvermin:
            new_n += digit
        else:
            continue

    if new_n == N:
        print(N)
        break
    else:
        N = str(int(N) - 1)