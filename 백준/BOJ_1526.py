N = input()

goldmin = ['4','7']
silvermin = ['1','2','3','5','6','8','9','0']

while True:
    new_n = ''
    for digit in N:
        if digit in goldmin and digit not in silvermin:
            new_n += digit
        else:
            continue

    if new_n == N:
        print(N)
        break
    else:
        N = str(int(N) - 1)



'''
N = int(input())

max_ = 4

for number in range(N+1):
    string_number = str(number)

    for char_number in string_number:
        #print(string_number, char_number)

        if not (char_number == '4' or char_number == '7'):
            break

        # for ~ else ~
        # for 이 정상적으로 다 완료되면 else가 실행된다.

    else:
        max_ = int(string_number)

print(max_)
'''