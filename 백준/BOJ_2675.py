T = int(input())

for i in range(T):
    a, b = map(str, input().split())

    for char in b:
        print(char*int(a), end='')
    print()
    