list_ = list(map(int, input().split()))

if sum(list_) >= 100:
    print('OK')
    
else:
    min_ = min(list_)
    if list_.index(min_) == 0:
        print('Soongsil')
    elif list_.index(min_) == 1:
        print('Korea')
    elif list_.index(min_) == 2:
        print('Hanyang')