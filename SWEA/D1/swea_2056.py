T = int(input())
date_of_month = {'01':31, '02':28, '03':31, '04':30, '05':31 , '06':30, '07':31, '08':31, '09':30, '10':31 , '11':30, '12':31}

for test_case in range(1, T+1):
    N = input()
    yy = N[0:4]
    mm = N[4:6]
    dd = N[6:8]

    if (mm in date_of_month) and (int(dd) <= date_of_month[mm]):
        print(f'#{test_case} {yy}/{mm}/{dd}')
    else:
        print(f'#{test_case} -1')
