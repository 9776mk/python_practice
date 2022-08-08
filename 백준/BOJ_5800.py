T = int(input())

for test_case in range(1, T+1):
    grade_ = list(map(int, input().split()))

    max_ = 0
    min_ = 100
    
    list_ = []
    for i in range(1, grade_[0]+1):
        list_.append(grade_[i])

    max_ = max(list_)
    min_ = min(list_)

    gap_list = []
    list_.sort(reverse=True)
    for i in range(len(list_)-1):
        gap_list.append(abs(list_[i] - list_[i+1]))
    
    max_gap = max(gap_list)

    print(f'Class {test_case}')
    print(f'Max {max_}, Min {min_}, Largest gap {max_gap}')