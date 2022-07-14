# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

word = input()
ind_a = 0
a_exist = False

for char in word:
    if char =='a':
        print(ind_a, end=' ')
        ind_a += 1
        a_exist = True
    else:
        ind_a +=1
        continue