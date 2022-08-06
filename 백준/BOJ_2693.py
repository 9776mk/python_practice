T = int(input())

for _ in range(T):
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)

    print(a_list[2])