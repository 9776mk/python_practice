# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

N = int(input())
cnt_len = 0
A = 1
# //를 사용

while N//A != 0:
    if(N//A) !=0:
        A *= 10
        cnt_len += 1
    else:
        break

print(cnt_len)

'''
1. 문자열로 형변환
print(len(str(number)))

2. 123 = 1 * 100 + 2 * 10 + 3 * 1
result = 0
#몫이 0이 되면 종료해야하니까!
while num :
# int : 0이 아닌 다른 수면 무조건 True!
while number != 0:
    number = number // 10
    cnt += 1

3. import math
print(int(math.log(number, 10))+1)

'''