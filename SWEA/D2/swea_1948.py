T = int(input())
date_list = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for test_case in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    total_days = 0

    for month in range(m1, m2):
        total_days += int(date_list[month])
    total_days += (d2-d1)+1

    print(f'#{test_case} {total_days}')