T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    prime_dict = {2 :0 ,3:0 ,5:0, 7:0, 11:0}
    is_True = True

    while is_True:
        for number in prime_dict.keys():
            if N % number==0:
                N /= number
                prime_dict[number] = prime_dict.get(number) +1
        
        if N == 1:
            is_True = False
            
    print(f'#{test_case}', end=' ')
    for key in prime_dict:
        print(prime_dict[key], end=' ')
    print()