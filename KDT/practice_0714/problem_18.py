# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = input()
dict_alpha = {}

for char in word:
    dict_alpha[char] = 0

for char in word:
    dict_alpha[char] += 1

for a in dict_alpha:
    print(a, dict_alpha[a])