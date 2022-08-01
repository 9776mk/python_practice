com_ = input()
list_com = []

while com_ != '고무오리 디버깅 끝':
    com_ = input()
    if com_ == '문제':
        list_com.append(com_)
    elif com_ == '고무오리':
        if len(list_com) != 0 :
            list_com.pop()
        else:
            list_com.append(com_)
            list_com.append(com_)
            continue

if len(list_com) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')