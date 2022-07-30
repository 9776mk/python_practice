# 두 숫자 A,B 를 입력받음
A, B = map(int, input().split())

# 수열을 B번째까지 만들어야 함
list_ = []

# 1 - 1개, 2-2개, 3- 3개, 4- 4개, n을 n번 반복하는 리스트를 생성
N = 1
is_True = True
while is_True:
    for i in range(N):
        list_.append(N)
        if len(list_) == B:
            is_True = False
            break
    N += 1
    
# A ~ B번째까지의 합 구하기
sum_ = 0
for i in range(A-1, B):
    sum_ += list_[i]
print(sum_)