# 공백이나 태그를 만나기 전까지 list에 차례대로 집어넣기
# 공백을 만나면 리스트가 빌때까지 pop 진행 후 새로운 문자열에 추가
# < 태그를 만나면 > 태그를 만나기 전까지 새로운 문자열에 추가

S = input()

list_ = list(S)

answer = ""

new_list = []
list_tag = []

for i in range(len(list_)):
    # '<' 기호일 때
    if list_[i] == '<':
        # 그동안 스택에 쌓인 문자열이 있다면 뒤집어서 추가
        while new_list:
            answer += new_list.pop()
        # list_tag 리스트가 비어있지 않게 추가
        list_tag.append(list_[i])
    # '>' 기호 일때
    elif list_[i] == '>':
        # list_tag를 비우고, 답에 '>'를 추가한 뒤 다음 문자열로 진행
        list_tag.pop()
        answer += '>'
        continue
    
    # 만약 list_tag가 비어있지 않으면, 즉 < 인 상태면 그대로 문자열 추가
    if list_tag:
        answer += list_[i]
    # 만약 list_tag가 비어있으면, 즉 <인 상태가 아니면
    else:
        # 공백을 만나면 그때까지 쌓은 문자열을 뒤집어서 추가
        if list_[i] == ' ':
            while new_list:
                answer += new_list.pop()
            # 후 공백도 추가
            answer+= ' '
        # 공백이 아닌 일반 문자를 만나면 list에 쌓아둠
        else:
            new_list.append(list_[i])

# 끝까지 돌았는데, 리스트가 비어있지 않은 경우 추가
if new_list != []:
    while new_list:
        answer += new_list.pop()

print(answer)