T = input()

# print(T.upper()) # 대문자 변경 메서드 사용

upper_T = ''

for char in T:
    if 97<= ord(char) <= 122:
        upper_T += chr(ord(char)-32)
    else:
        upper_T += char

print(upper_T)