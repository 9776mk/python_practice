# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

word = input()
rev_word = ""

for i in range(len(word)-1,-1,-1):
    rev_word += word[i]

print(rev_word)