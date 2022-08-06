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

#is_possible에서 bool 대신 그냥 문자열로 설정해도 됨



'''
# input() : 느리다
# sys.stdin.readline() " 빠르다


stack_list = [11,10,8,5]

answer = 'Yes'

comparison = stack.pop()

for stack in stack_list
# 스택이 비어있지 않을 때 까지
    while len(stack) != 0
        # top comparison 비교
        if stack[-1] > comparison:
            # pop을 사용해서 comarison 값을 갱신
            comparison = stack.pop
        else:
            answer = 'No'
            break
'''