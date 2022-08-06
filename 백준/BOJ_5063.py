N = int(input())
for _ in range(N):
    cost_ = list(map(int, input().split()))
    if cost_[0] < cost_[1] - cost_[2]:
        print('advertise')

    elif cost_[0] == cost_[1] - cost_[2]:
        print('does not matter')

    elif cost_[0] > cost_[1] - cost_[2]:
        print('do not advertise')