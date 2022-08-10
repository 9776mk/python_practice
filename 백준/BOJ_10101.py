angle = []
for _ in range(3):
    angle.append(int(input()))

total = sum(angle)
pcs = []

if total != 180:
    print('Error')
else:
    for num in angle:
        pcs.append(angle.count(num))
    
    if 3 in pcs:
        print('Equilateral')
    elif 2 in pcs:
        print('Isosceles')
    else:
        print('Scalene')