N = input()
new_N = ''
cnt = 0


while True:
    if int(N) < 10:
        N = '0' + N
        print(N)
        break
    else:
        new_N = 10