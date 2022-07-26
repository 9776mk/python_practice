T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    prime_number_list = [2,3,5,7,11]
    new_dict = {2 :0 ,3:0 ,5:0, 7:0, 11:0}
    is_True = True

    while is_True:
        for number in new_dict.keys():
            if N % number==0:
                N /= number
                new_dict[number] = new_dict.get(number) +1
        
        if N == 1:
            is_True = False
            
    print(f'#{test_case}', end=' ')
    for key in new_dict:
        print(new_dict[key], end=' ')
    print()