A, B, C = map(int, input().split())

# a,b,c의 범위를 숫자로 만든 뒤
# set 합집합을 구한다.

start, end = map(int,input().split())
a_set = set(range(start, end))

start, end = map(int,input().split())
b_set = set(range(start, end))

start, end = map(int,input().split())
c_set = set(range(start, end))

set_all = a_set | b_set | c_set
# print(set_all)
set_3 = a_set & b_set & c_set
print(set_3)
set_2 = ((a_set & b_set) | (b_set & c_set) | (c_set & a_set)) - set_3
print(set_2)
set_1 = set_all - set_3 - set_2
print(set_1)

sum_ = len(set_1) * A + len(set_2) * (B*2) + len(set_3) * (C*3)

print(sum_)