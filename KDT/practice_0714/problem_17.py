# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# ord(a)~ord(z) = 97 ~ 122
# ord(A)~ord(Z) = 65 ~ 90
# ord(a) - 32  = ord(A)


word = input()
upper_word = ''

for char in word:
    upper_word += chr(ord(char)-32)

print(upper_word)