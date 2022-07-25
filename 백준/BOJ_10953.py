T = int(input())

for test_case in range(T):
    # ,로 나눠진 a,b를 입력 받음
    a, b = map(int, input().split(','))
    print(a + b)