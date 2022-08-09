vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
text_ =''

while True:
    cnt = 0
    text_ = input()

    if text_ == '#':
        break
    else:
        for text in text_:
            if text in vowel:
                cnt += 1

        print(cnt)