colors_ = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4, 'green' : 5, 'blue':6, 'violet':7,'grey':8, 'white':9}

list_ = []

for i in range(3):
    n = input()
    list_.append(colors_[n])

print((list_[0]*10 + list_[1])*10**(list_[2]))