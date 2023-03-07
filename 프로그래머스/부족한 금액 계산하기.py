def solution(price, money, count):
    sum = 0

    for i in range(1, count + 1):
        sum += i * price

    if sum > money:
        answer = sum - money

    else:
        answer = 0

    return answer


print(solution(3, 20, 4))
