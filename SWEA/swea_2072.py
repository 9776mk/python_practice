T = int(input())

for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    sum = 0

    for number in N:
        if number % 2 != 0:
            sum += number
        else:
            continue

    print(f'#{test_case} {sum}')

