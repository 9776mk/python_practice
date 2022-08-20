list_ = []

for i in range(1, 6):
    name_ = input()
    if 'FBI' in name_:
        list_.append(i)

if len(list_) == 0:
    print('HE GOT AWAY!')
else:
    for name in list_:
        print(name)