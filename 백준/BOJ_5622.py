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
# 알파벳 묶음을 만듦
dial_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# 걸리는 시간 : 3      4      5      6      7      8       9      10

# 사용자로부터 입력
words = input()

# 총 걸리는 시간 선언
time_ = 0

# dial_list에 있는 알파벳들을
for alphabet in dial_list:
    # 한 글자씩 분리하고
    for j in alphabet:
        # words 단어를 한 글자씩 분리해서
        for k in words:
            # 만약 두 글자가 같으면
            if j == k:
                # dial_list의 인덱스 값 + 3을 time_변수에 더한다.
                time_ += dial_list.index(alphabet) + 3

print(time_)
'''