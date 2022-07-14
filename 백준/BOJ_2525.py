A, B = map(int, input().split())
C = int(input())
h, m =  0, 0

h = int(C/60) # C를 60으로 나눈 몫, 시간
m = C % 60 # C를 60으로 나눴을 때의 나머지, 분

A = (A+h)%24
B = B + m

if B<60:
    print(A%24, B)
else:
    print((A+1)%24, B%60)