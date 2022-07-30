N = int(input())
n_list = list(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

n_dict = {}

# N개의 숫자와 갯수를 딕셔너리 형태로 저장
for i in n_list:
    n_dict[i] = n_dict.get(i, 0) +1

# m_list에 있는 원소들을 key로 value를 불러옴. 없으면 0으로
for j in m_list:
    print(n_dict.get(j, 0), end=' ')