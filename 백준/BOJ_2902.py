# 문자를 입력 받음
names = input()
# 새로운 문자열 선언
new_names_ = ''
# ord('A') ~ ord('Z') 65 ~ 90

# 글자를 검사
for alpha in names:
    # A와 B 사이의 아시크 코드 값이면
    if 65 <= ord(alpha) <= 90 :
        # 새로운 문자열에 추가
        new_names_ += alpha
    else:
        continue
# 출력
print(new_names_)