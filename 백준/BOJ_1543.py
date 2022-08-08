str_ = input()
word_ = input()

str_len = len(str_)
word_len = len(word_)
idx_ = 0
cnt = 0

print(str_len, word_len, idx_, cnt)


# 0부터 시작해서
while True:
    if word_ == str_[idx_:word_len]:
        print(str_[idx_:word_len])
        cnt += 1
        idx_ += word_len
    else:
        print(str_[idx_:word_len])
        idx_ += 1

    if idx_ == str_len - word_len + 1:
        break

print(cnt)