T = int(input())

for test_case in range(1,T+1):
    S = input()
    nod  = 0
    
    #마디 수 1~10이므로 한 글자부터 열 글자까지 반복
    for i in range(1, 11):  
        # 첫 번째 단위와 두 번째 단위가 같으면
        if (S[0:i] == S[i:2*i]): 
            nod = i
            break
            
    print('#%d %d' %(test_case, nod))