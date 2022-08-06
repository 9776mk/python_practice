N = int(input())

for _ in range(N):
    str_ = input()
    vps_list = []
    is_vps = True

    # 입력받은 문자열에 대해
    for str in str_:
        # 만약 문자열이 '(' 라면 vps_list에 추가
        if str == '(':
            vps_list.append(str)
        # 문자열이 ')'일 때
        else:
            # vps_list가 0이 아니면, vps_list에서 pop
            if len(vps_list) != 0:
                vps_list.pop()
            # vps_list가 이미 0이라면, 즉 ')'가 더 많으므로 중지하고 False로 바꿈
            else:
                is_vps = False
                break
    # len(vps_list)가 0이 아닌 경우는 '('의 갯수가 더 많은 경우
    if is_vps == True and len(vps_list) == 0:
        print('YES')
    else:
        print('NO')

'''

# 문자열의 경우 상수로 만들면 실수를 줄일 수 있다.

LEFT = '('
RIGHT = ')'

brackets = ['(',')']
left_stack = []
right_stack = []

for bracket IN brackets:
    # 괄호가 좌괄호이면

    if bracket == LEFT:
        # left stack push
        left_stack.append(bracket)
    
    if bracket == RIGHT:
        # 좌괄호 스택의 길이가 0이 아닐 때
        # 좌괄호 스택이 비어있지 않을 때
        if len(left_stack) != 0:
            left_stack.pop()

        # 우괄호를 우괄호 스택에 push
        else:
            right_stack.append(bracket)

if len(left_stack) == 0 and len(right_stack) == 0:
    print('yes')
else:
    print('no')
'''