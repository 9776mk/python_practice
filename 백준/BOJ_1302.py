N = int(input())

# 판매 리스트 저장
sold_dict = {}

# 책 판매 저장
for _ in range(N):
    title_ = input()
    sold_dict[title_] = sold_dict.get(title_, 0) +1

# 최대 판매 책을 넣기
max_title = ''
max_num = 0

for k, v in sold_dict.items():
    if v > max_num:
        max_title = k
        max_num = v

    # print('a' < 'b') # True
    # print('aa' < 'ab') # True
    # 사전 상 앞에 있는 단어가 더 작음
    elif v == max_num:
        if k < max_title:
            max_title = k
            max_num = v

print(max_title)