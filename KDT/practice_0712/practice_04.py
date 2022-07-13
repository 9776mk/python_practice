# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

n = 5
sum1 = 1
sum2 = 1
count = 1

while count<=n:
    sum1 *= count
    count += 1

for i in range(1,n+1):
    sum2 *= i



print(f'while문 합 : {sum1}')
print(f'for문 합 : {sum2}')