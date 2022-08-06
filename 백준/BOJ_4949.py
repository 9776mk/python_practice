is_done = True
sent_ = ''

while is_done:
    # 소괄호와 대괄호를 저장할 리스트 선언
    list_ = []

    is_balanced = True

    sent_ = str(input())

    if sent_ == '.':
        is_done = False
        break

    else:
        for alpha in sent_:
            if alpha == '(' or alpha == '[':
                list_.append(alpha)

            elif alpha== ')':
                if len(list_) != 0 and list_[-1] == '(':
                    list_.pop()
                else:
                    is_balanced = False
                    break

            elif alpha== ']':
                if len(list_) != 0  and list_[-1] == '[':
                    list_.pop()
                else:
                    is_balanced = False
                    break

        if is_balanced == True and list_ == []:
            print('yes')
        else:
            print('no')