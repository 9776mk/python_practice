# 숫자를 str로 바꾼뒤 슬라이싱으로 뒤집고, int형을 변환하는 Rev함수 선언
# '001'을 int형으로 변환하면 '1'이 됨
def Rev(num):
    num = str(num)
    rev_num = int(num[::-1])
    return rev_num

X, Y = map(int, input().split())

print(Rev(Rev(X)+Rev(Y)))