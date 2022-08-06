import sys
input = sys.stdin.readline


T = int(input())

for test_case in range(T):
    n1 = int(input())
    n1_list = list(map(int, input().split()))
    n1_set = set(n1_list)
    print(n1_set)


    n2 = int(input())
    n2_list = list(map(int, input().split()))
    n2_set = set(n2_list)


    for number in n2_list:
        if number in n1_set:
            print(1)
        else:
            print(0)