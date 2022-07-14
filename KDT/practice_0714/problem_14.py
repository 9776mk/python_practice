# 문자열 word가 주어질 때, 해당 문자열에서 `a` 개수를 구하세요.
# `count()` 메서드 사용 금지**

word = input()
cnt_a = 0

for char in word:
    if char =='a':
        cnt_a +=1
    else:
        continue

print(cnt_a)