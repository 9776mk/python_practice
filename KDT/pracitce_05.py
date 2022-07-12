# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = [3, 10, 20]
sum = 0
count = 0

# 총 합을 구하는 코드
for n in numbers:
    sum += n

# 멤버의 수를 구하는 코드
for i in numbers:
    count += 1

#평균을 구하는 코드 (int형으로 변환)
avg = int(sum / count)

print(avg)