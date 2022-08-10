text = input()

happy_ = text.count(':-)')
sad_ = text.count(':-(')

if happy_ == 0 and sad_ == 0:
    print('none')
elif happy_ == sad_:
    print('unsure')
elif happy_ > sad_:
    print('happy')
elif happy_ < sad_:
    print('sad')