N = int(input())

dict_ = {}
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    # 만약 a가 딕셔너리 안에 있고
    if a in dict_.keys():
        # a의 밸류가 b가 아니라면
        if dict_[a] != b:
            # a의 밸류를 b로 바꾸고
            dict_[a] = b
            # 갯수 +1
            cnt += 1
        else:
            continue

    # a가 딕셔너리 안에 없다면
    else:
        # 키 a의 밸류값을 b로 설정
        dict_[a] = b

    print(cnt)