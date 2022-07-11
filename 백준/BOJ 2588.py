a = input()
b = input()

int_a = int(a)
int_b = int(b)

list_b = list(b)

val_1 = int_a * int(list_b[2])
val_2 = int_a * int(list_b[1])
val_3 = int_a * int(list_b[0])

sum_val = val_1 + 10 * val_2 + 100 * val_3


print(val_1)
print(val_2)
print(val_3)
print(sum_val)