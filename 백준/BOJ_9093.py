T = int(input())


for _ in range(T):
    list_ = list(map(str, input().split()))
    rev_list = [0] * len(list_)

    for i in range(len(list_)):
        for j in range(1, len(list_[i])+1):
            print(list_[i][len(list_[i])-j], end='')
        print(end=' ')
    print()