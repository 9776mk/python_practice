from pprint import pprint


T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    n_list = [list(input().split()) for _ in range(n)]

    #print(n_list)

    new_list = [[0]*n for _ in range(n)]

    # 오른쪽으로 한 번 회전하는 함수
    def rotate_ (list_):
        n = len(list_)

        rotated_ = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n): 
                rotated_[i][j] = list_[n-j-1][i]

        return rotated_

    # 오른쪽으로 1,2,3번 실행한 후 같은 행에 추가
    # 1. 90, 180, 270의 결과값을 저장하는 리스트를 따로 만든 뒤 한 번에 저장 - 코드를 세 번 적기. 결과 리스트 하나 더
    # 결과 리스트 = n행 3열
    result_ = [[0] * 3 for _ in range(n)]

    # 회전한 리스트 저장
    list_90  = rotate_(n_list)
    list_180 = rotate_(list_90)
    list_270 = rotate_(list_180)


    # 결과 리스트에 각 행들을 추가
    # [0][0] = 90도 0행 [0][1] = 180도 0행 [0][2] = 270도 0행
    # ...
    # [n-1][0] = 90도 n-1행 [n-1][1] = 180도 n-1행 [n-1][2] = 270도 n-1행

    # 행 : 0 ~ n-1
    # 열 : 3
    for i in range(n):
        for j in range(3):
            if j == 0:
                result_[i][j] = ''.join(list_90[i])
            elif j == 1:
                result_[i][j] = ''.join(list_180[i])
            elif j == 2:
                result_[i][j] = ''.join(list_270[i])


    print(f'#{test_case}')
    for i in range(n):
        k = ' '.join(map(str, result_[i]))
        print(k)

#print(result_)





# # 2. 한 번씩 실행한 후 계속해서 추가 - for문 활용, 결과 리스트 하나만 있으면 됨
# # 함수 3번 돌리고, 그 리스트들을 행별로 추가.
# result_ = [[0] * 3 for _ in range(n)]









# print(rotate_(n_list))

