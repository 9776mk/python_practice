# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

# 1234 혹은 4자리숫자만 가능
# num = 1234
# new_num = 0
# multiple_num = 1000

# while multiple_num != 0:
#     new_num += (num % 10)*multiple_num
#     num //= 10
#     multiple_num = int(multiple_num / 10)

# print(new_num)

# num의 자릿수와 상관없이 가능
num = int(input())
new_num = 0

num_for_digit = num
digit_num = 1
while num_for_digit//10 != 0:
    digit_num += 1
    num_for_digit//=10

for i in range(digit_num):
    a = num % 10
    new_num += a * 10**(digit_num-1-i)
    num //= 10

print(new_num)


'''
1. 문자열
print(str(number[::-1]))

2.
number =123
result = 0
while number:
    #이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += number %10
    # number를 깍는다.
    number //=10

print(result)




'''
