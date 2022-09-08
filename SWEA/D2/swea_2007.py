T = int(input())

for test_case in range(1,T+1):
    S = input()
    max_n  = 0
    
    for i in range(1, 11):  #마디 수 1~10
        for j in range(0,1): 
            if (S[j*i:(j+1)*i] == S[i*(j+1):i*(j+2)]):
                max_n = i
                break
            else:
                continue
        if(max_n!=0):
            break
    print('#%d %d' %(test_case, max_n))