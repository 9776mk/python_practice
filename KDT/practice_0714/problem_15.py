# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.

word = input()
ind_a = 0
a_exist = False

for char in word:
    if char =='a':
        print(ind_a)
        a_exist = True
        break
    else:
        ind_a +=1
        continue

if a_exist == False and ind_a == len(word):
    print(-1)