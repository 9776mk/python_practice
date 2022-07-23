A, B, C = map(int, input().split())
# A + B*N = C*N 일때 N으로 출력하면 예제 3번에서 시간 초과
# A + (B - C) * N = 0
# N = A/(C-B)

if B > C:
    print(-1)
else:
    print(int(A/(C-B))+1)