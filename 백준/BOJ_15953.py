T = int(input())

reward_2017 = [[1,500], [3,300],[6,200],[10,50],[15,30],[21,10]]
reward_2018 = [[1,512],[3,256],[7,128],[15,64],[31,32]]


for _ in range(T):
    a, b = map(int, input().split())

    total_reward = 0

    for i in range(6):
        if a == 0:
            break

        elif a <= reward_2017[i][0]:
            total_reward += reward_2017[i][1]
            break
    
    for j in range(5):
        if b == 0:
            break

        if b <= reward_2018[j][0]:
            total_reward += reward_2018[j][1]
            break

    print(total_reward * 10000)