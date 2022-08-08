N = int(input())

cnt_ = 0
a = 1

while True:
    a += 1
    if '666' in str(a):
        cnt_ += 1
        if cnt_ == N:
            print(a)
            break