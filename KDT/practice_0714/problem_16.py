# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지
word = input()
vowel = ['a', 'e', 'i', 'o', 'u']
cnt_vowel = 0

for i in range(len(vowel)):
    for j in range(len(word)):
        if vowel[i] == word[j]:
            cnt_vowel +=1 

print(cnt_vowel)