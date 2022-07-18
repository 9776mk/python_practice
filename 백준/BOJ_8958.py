T = int(input())

for test_case in range(T):
    ans = input()
    o_list = []
    sum_num = 0
    sum_tmp = 0

    for i in range(len(ans)):
        if ans[i] == 'O':
            o_list.append('O')

            if i == len(ans)-1: 
                for i in range(1, len(o_list)+1):
                    sum_tmp += i
                sum_num += sum_tmp


        else:
            if len(o_list) == 0:
                continue
            else:
                for i in range(1, len(o_list)+1):
                    sum_tmp += i
                sum_num += sum_tmp
                sum_tmp = 0
                o_list = []
    print(sum_num)

# [OO, O, OOO] -> 글자수만큼 더하면 된다.