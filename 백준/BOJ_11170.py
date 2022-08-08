T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    sum_0 = 0

    for i in range(n, m+1):
        str_i = str(i)
        for num in str_i:
            if num == '0':
                sum_0 += 1

    print(sum_0)