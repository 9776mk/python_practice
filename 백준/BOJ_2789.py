word = input()
censorship = 'CAMBRIDGE'

censored_word = []

for char in word:
    if char not in censorship:
        censored_word.append(char)
    else:
        continue

print("".join(censored_word))