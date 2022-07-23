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
            num_dict[char] = num_dict.get(char, 0) +1
        
    print(f'#{test_case} {new_N}')

'''
# Input 가져오기 (첫번째 값 -> 1)
N = int(input())
# set에 계속 추가 예정
number = set()
# while 반복 => set의 길이가 10이 될 때까지
    while len(numbers) < 10:
    # for 반복 : 숫자를 문자로
    for n in str(N):
    # numbers set에 계속 추가
        numbers.add(n)
'''