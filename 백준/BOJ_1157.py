# 알파벳 대, 소문자가 구별없이 주어짐
S = input() 

S_num = {}
max = 0
max_alphabet = ''

# 문제에서는 대소문자 구분을 하지 않으므로, 입력 받은 문자를 전부 대문자로 바꿈
S = S.upper()

# 딕셔너리에 input 값을 집어넣어 나타난 횟수 구하기
for char in S :
    S_num[char] = S_num.get(char, 0) + 1 # 키 값에 대응되는 value값들을 전부 딕셔너리로 저장

# 가장 많이 사용된 알파벳 찾기
# S_num 에는 1 이상씩 들어있으므로 max = 0으로 설정해도 무관
for char in S_num:
    if S_num[char] > max: #문자값의 개수가 0보다 크면
        max = S_num[char]
        max_alphabet = char
    elif S_num[char] == max: # 문자값의 개수가 같은 것이 있으면 
        max_alphabet = '?' 
    else:
        continue

print(max_alphabet)