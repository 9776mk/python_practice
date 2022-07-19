A, B = map(int, input().split())
rev_A, rev_B = 0, 0

while A:
    # number가 123인 경우 

    #이전 결과에 10을 곱하고
    rev_A *= 10
    # 나머지를 더해주고
    rev_A += A %10
    # number를 깍는다.
    A //=10

while B:
    #이전 결과에 10을 곱하고
    rev_B *= 10
    # 나머지를 더해주고
    rev_B += B %10
    # number를 깍는다.
    B //=10

print(rev_A if rev_A > rev_B else rev_B)
