K = int(input())
S = input()

num = len(S) // K
list_ = []

for i in range(num):
    if i%2 == 0:
        list_.append(S[K*i:K*(i+1)])
    else:
        list_.append(S[K*(i+1)-1:K*i-1:-1])
        

for i in range(K):
    for j in range(num):
        print(list_[j][i], end='')