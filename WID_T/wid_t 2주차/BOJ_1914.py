def hanoiTop(start, inter, end, count):
    if count == 1:
        print(start, end)
        return
    
    # 원판 n-1개를 두 번째 기둥으로 옮기기
    hanoiTop(start, end, inter, count-1)
    print(start,end)
 
    # 두 번째 기둥에 있는 원판을 마지막 기둥으로 옮기기
    hanoiTop(inter, start, end, count-1)
 
n = int(input())

# 하노이탑을 완성하는 데 드는 횟수
print(2 ** n - 1)
# n이 20 이하일 때만 과정 출력
if n <= 20:
    hanoiTop(1, 2, 3, n)
