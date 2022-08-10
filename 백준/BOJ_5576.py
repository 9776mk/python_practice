w_ = []
k_ = []

for _ in range(10):
    w_.append(int(input()))

for _ in range(10):
    k_.append(int(input()))

w_.sort(reverse=True)
k_.sort(reverse=True)

sum_w, sum_k  = 0, 0

for i in range(3):
    sum_w += w_[i]
    sum_k += k_[i]

print(sum_w, sum_k)