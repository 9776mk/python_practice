# 나머지를 저장하는 dict 선언
remains_dict = {}

# 10번 반복
for i in range(10):
    # 입력을 받고
    N = int(input())
    # N을 42로 나눈 나머지를 저장
    remain_N = N % 42
    # remain_dict에 똑같은 값이 있으면 +1 없으면 value값을 0으로 생성
    remains_dict[remain_N] = remains_dict.get(remain_N, 0) + 1

# reamin_dict의 길이를 출력
print(len(remains_dict.keys()))


'''
list와 set을 이용한 풀이

num_list = []
remain_list = []

for i in range(10):
    N = int(input())
    num_list.append(N)

#print(num_list)

for num in num_list:
    remain_list.append(num%42)

remain_list = set(remain_list)

print(len(remain_list))
'''