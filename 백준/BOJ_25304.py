x = int(input())
n = int(input())

sum_ = 0

for _ in range(n):
    a, b = map(int, input().split())
    sum_ += (a * b)

print('Yes' if x == sum_ else 'No')