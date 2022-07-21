T = int(input())

for test_case in range(1, T+1):
    N = input()
    new_N = int(N)
    num_dict = {}
    A = 1

    while len(num_dict) != 10:
        new_N = int(N) * A
        A += 1
        for char in str(new_N):
            num_dict[char] = num_dict.get(char, 0)+1
        
    print(f'#{test_case} {new_N}')