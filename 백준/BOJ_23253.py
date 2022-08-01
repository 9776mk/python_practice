import sys
# 빠른 입력
input = sys.stdin.readline

# 교과서 수 N, 교과수 더미 수 M
N, M = map(int, input().split())
stack_ = []
is_possible = True

for i in range(M):
    ki = int(input())
    stack_.append(list(map(int, input().split())))

for i in range(M):
    for j in range(len(stack_[i]) - 1):
        if stack_[i][j] < stack_[i][j + 1]:
            is_possible = False

if is_possible:
    print('Yes')
else:
    print('No')