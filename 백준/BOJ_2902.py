# 문자를 입력 받음
# names = input()
names = 'Knuth-Morris-Pratt'
new_names_ = ''
# ord('A') ~ ord('Z') 65 ~ 90
print(ord('A'))
print()


# 글자를 검사
for alpha in names:
    if 65 <= ord(alpha) <= 90 :
        new_names_ += alpha
    else:
        continue
# 출력
print(new_names_)