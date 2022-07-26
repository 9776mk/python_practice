# N = int(input())
# list_N = list(map(int, input().split()))

N = 5
list_N = [1,2,1,4,6]
gap_N = []
tmp_sum = 0
sum = 0

for i in range(N-1):
    gap_N.append(list_N[i+1] - list_N[i])

gap_N.append(0)

for number in gap_N:
    if number > 0:
        tmp_sum += int(number)
    else:
        if tmp_sum > sum:
            sum = tmp_sum

print(sum)