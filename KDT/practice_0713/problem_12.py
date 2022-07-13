# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = input()
a_removed_word = ""

for char in word:
    if char =='a':
        continue
    else:
        a_removed_word += char

print(a_removed_word)