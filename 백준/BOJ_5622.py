S = input()

# 1. 하나씩 대응
# sum = 0
# for char in S:
#     if char == 'A' or char =='B' or char =='C':
#         sum += 1
#     elif # 이런 식으로 전개 가능

# 키값이 리스트가 되야하므로 딕셔너리는 불가
# 다대일 대응이 가능한 것?
# 2. ord(A) 65 ~ ord(Z) 90으로 그나마 간단하게 가능할 것 같다.

sum = 0
for char in S:
    if 65<= ord(char) <= 67:
        sum += 3
    elif ord(char) <=70:
        sum += 4
    elif ord(char) <=73:
        sum += 5
    elif ord(char) <=76:
        sum += 6
    elif ord(char) <=79:
        sum += 7
    elif ord(char) <=83:
        sum += 8
    elif ord(char) <=86:
        sum += 9
    elif ord(char) <=90:
        sum += 10

print(sum)

'''
3. https://ooyoung.tistory.com/73
alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] # 알파벳 묶음들을 만듦
word = input() # 입력 받음
time = 0 # 걸리는 시간 저장

for unit in alpabet_list : # alphabet 전체 리스트 꺼냄 
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
print(time)
'''