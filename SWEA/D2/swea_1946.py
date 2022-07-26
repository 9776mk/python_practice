T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    origin_doc = ''

    # origindoc에 글자 채워넣기
    for i in range(N):
        ci, ki = input().split()
        origin_doc += ci * int(ki)        

    # 10글자씩 잘라서 출력하기
    total_len = len(origin_doc)
    rep_time = total_len // 10
    rest = total_len % 10

    for i in range(rep_time):
        print(origin_doc[10*i: 10*(i+1)])
    print(origin_doc[10*rep_time:10*rep_time+rest+1])

        
        
