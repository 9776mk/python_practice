M = int(input())

cup_ = [[1], [0], [0]]
tmp_ = [0,0]

for _ in range(M):
    a,b = map(int, input().split())

    a -= 1
    b -= 1

    cup_[a], cup_[b] = cup_[b], cup_[a]
    
    #print(cup_[a], cup_[b])

for i in range(3):
    if cup_[i][0] == 1:
        print(i+1)