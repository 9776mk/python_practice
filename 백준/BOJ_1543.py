str_ = input()
word_ = input()

str_len = len(str_)
word_len = len(word_)

idx_ = 0
cnt = 0

# 0부터 시작해서
# 
while idx_ <= str_len - word_len:
    #print(str_[idx_:idx_+ word_len])
    if str_[idx_:idx_+ word_len] == word_ :
        cnt += 1
        idx_ += word_len
    else:
        idx_ += 1

print(cnt)


'''
a = input()
b = input()
print(a.count(b))
'''