T = int(input())

for test_case in range(1,T+1):
    S = input()
    nod  = 0
    
    #마디 수 1~10이므로 한 글자부터 열 글자까지 반복
    for i in range(1, 11):  
        for j in range(0,1):
            # 총 2번 체크
            # 예를 들어 마디가 1일 때
            # S[0]과 S[1]이 같다면 S[2]와 S[3]이 같아야 마디이므로
            # aab 같은 예외를 처리할 수 있음. 
            if (S[i*j:(j+1)*i] == S[i*(j+1):i*(j+2)]):
                nod = i

                break
            else:
                continue
        # 마디를 찾았다면 종료
        if(nod != 0):
            break
            
    print('#%d %d' %(test_case, nod))