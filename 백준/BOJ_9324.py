t = int(input())

for _ in range(t): 
    sum_ = 0
    s = int(input())
    sum_ += s
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        sum_ += a * b
    print(sum_)
