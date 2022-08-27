
T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    print(f'{test_case}')
    
    # N=1인 경우 1 출력
    if(N == 1):
        print(1)
    # N=2인 경우 1, 1, 1 출력
    elif (N==2):
        print(1)
        print(1,1)
    # N이 1,2가 아닌 경우
    else:
        # 2차원 리스트로 생성 후
        pascal = [[] for _ in range(N)]
        # 첫 번째와 두 번째 리스트에 값 저장
        pascal[0] = [1]
        pascal[1] = [1,1]
    	
        # 다음줄을 위한 for문
        # 2면 1번 진행, 3이면 2번 진행, n이면 n-1번 진행하므로
        # 2부터 N-1까지 진행
        for i in range(2, N): 
            # 다음줄을 생성하기 위해 참고하는 윗줄
            # 1부터 i+1까지 총 i번 반복
            for j in range(1, i+2):
                # 처음에 1 추가 
                if (j==1):
                    pascal[i].append(1)
                # 마지막에 1 추가
                elif (j==i+1):
                    pascal[i].append(1)
                # 처음과 마지막이 아니라면
                else: 
                    # 윗줄의 j-2번째 인덱스와 j-1의 인덱스를 합침
                    pascal[i].append(pascal[i-1][j-2] + pascal[i-1][j-1]) 

        # 2차원 리스트의 값들을 하나씩 출력
        for i in range(0, N):
            for j in range(0, i+1):
                print(pascal[i][j], end=" ")
            if(j!=i+1):
                print()
            else:
                break