list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

sum_A = 0
sum_B = 0

Awin_index = 0
Bwin_index = 0



for i in range(10):
    if list_A[i] > list_B[i]:
        sum_A += 3
        Awin_index = i
    elif list_A[i] < list_B[i]:
        sum_B += 3
        Bwin_index = i
    else:
        sum_A += 1
        sum_B += 1

print(sum_A, sum_B)

if sum_A > sum_B:
    print('A')
elif sum_A < sum_B:
    print('B')
elif (sum_A == sum_B) and (Awin_index != Bwin_index):
    print('A' if Awin_index > Bwin_index else 'B')
else :
    print('D')