A, B = map(int, input().split())

# 둘 중 하나가 1이면 
if A == 1 or B == 1:
    print(1)
    print(A * B)

else:
    # GCD : The Greatest Common Denominator 최대 공약수
    gcd_AB = 1
    # LCM : The Least Common muliple 최소 공배수
    lcm_AB = 1

    # 소인수 : prime factor
    prime_A, prime_B = {}, {}
    n_A, n_B = 2, 2 

    # 소인수 분해 코드
    # ex) 24 = 2**3 * 3**1 => {2:3, 3:1}
    while A != 1:
        if A % n_A == 0:
            prime_A[n_A] = prime_A.get(n_A, 0)+1
            A //= n_A
        else:
            n_A += 1
    # 18 = 2**1 * 3**2 => {2:1, 3:2}
    while B != 1:
        if B % n_B == 0:
            prime_B[n_B] = prime_B.get(n_B, 0)+1
            B //= n_B
        else:
            n_B += 1

    # gcd 코드 
    # ex) gcd(24, 18) = 2 * 3
    # gcd는 공통된 최소의 약수를 곱하면 됨
    for i in prime_A.keys():
        if i in prime_B.keys():
            gcd_AB *= i ** min(prime_A[i], prime_B[i])

    # lcm 코드
    # ex) lcm(24, 18) = 2**3 * 3**2
    # prime_A를 기준으로
    for i in prime_A.keys():
        # key값이 공통으로 있다면 둘 중 더 큰 value값을 곱함
        if i in prime_B.keys():
            lcm_AB *= i ** max(prime_A[i], prime_B[i])
        # key값이 A에만 들어있다면(A에만 들어있는 약수라면), lcm에 i**1 즉, i를 곱함
        else:
            lcm_AB *= i ** prime_A[i]
    # prime_B를 기준으로
    for i in prime_B.keys():
        # pirme_B에만 들어있는 값을 곱해줌
        if i not in prime_A.keys():
            lcm_AB *= i ** prime_B[i]
        else:
            continue

    print(gcd_AB)
    print(lcm_AB)

'''
# 시간 초과
# GCD : The Greatest Common Denominator 최대 공약수
gcd_AB = 0
# LCM : The Least Common muliple 최소 공배수
lcm_AB = 0


# 공약수를 찾는 방법 -> 1부터 최솟값까지 각각 0으로 나눴을 때 나눠 떨어지는 수
for denom in range(1,(min(A,B))):
    if A % denom == 0 and B % denom ==0:
        gcd_AB = denom

# A*B부터 max(A,B)까지 거꾸로 공통된 배수 찾기
for multiple in range(A*B, max(A,B), -1):
    if multiple % A == 0 and multiple % B == 0:
        lcm_AB = multiple

print(gcd_AB)
print(lcm_AB)
'''