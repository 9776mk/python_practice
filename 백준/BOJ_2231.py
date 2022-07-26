N = input()
first_N = int(N)
decom_num = 0

while int(N) != 0:
    N = str(int(N)-1)
    # 계산 반복을 위해 0으로 초기화
    total_num = 0

    # 각 자릿수의 합
    for number in N:
        total_num += int(number)
    
    # 분해합이 있는지 없는지 검사 ex) 215 + 2 + 1 + 5 =? 216
    if first_N == int(N) + total_num :
        decom_num = int(N)
    
print(decom_num)