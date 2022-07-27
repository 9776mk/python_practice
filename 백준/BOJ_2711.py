T = int(input())

for i in range(T):
    a, b = input().split()
    b = list(b)
    b.pop(int(a)-1)
    print("".join(b))