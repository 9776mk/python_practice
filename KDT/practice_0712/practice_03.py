# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

n = 10
count = 0
sum1 = 0
sum2 = 0

# while 문
while count <= 10:
    sum1 += count
    count += 1

for i in range(n+1):
    sum2 += i

print(f'while문 합 : {sum1}')
print(f'for문 합 : {sum2}')