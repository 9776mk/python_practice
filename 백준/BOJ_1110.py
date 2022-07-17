# N = str(input()) # N을 문자열로 입력

# RN = int(N) # RN은 int형
# N2 = None # N2는 None을 저장

# if int(N) < 10: # N이 10보다 작은 경우
#     N='0' + N # 앞에 0 추가

# count = 0 # 카운트 초기값 = 0

# while N2 != RN:# 
#     R = int(N[0]) + int(N[1]) # 십의 자리 N[0]와 일의자리 N[1]를 더한 값을 R에 저장하고
#     R = str(R) # R을 문자열로 변환
#     if int(R) <10: # 만약 새로운 R이 10보다 작다면
#         R = '0'+ R # 앞에 0을 붙임
#     N = N[1] + R[1] # 새로운 N은 입력된(오래된)의 일의자리와 새로운 숫자 R의 일의자리의 합(문자열)
#     N2 = int(N) #(N2는 N의 int값)

#     count += 1 # N2와 RN이 일치할 때 까지 +1

# print(count)





N = input()
n_first = int(N)
count = 0
new_n = 0
next_n = 0


if len(N) < 2:
    N = '0' + N

while new_n != n_first:
    new_n = int(N[0]) + int(N[1])
    new_n = str(new_n)

    if len(new_n) < 2:
        new_n = '0' + new_n

    next_n = N[1]+ new_n[1]
    new_n = int(next_n)
    count += 1
