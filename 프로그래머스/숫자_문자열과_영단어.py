num_dict = {'zero' : 0 , 'one' : 1 , 'two' : 2 , 'three' : 3 ,'four' : 4, 'five' : 5 , 'six' : 6 , 'seven' : 7 , 'eight' : 8 , 'nine' : 9 }

s = input()

answer = ''

num_list = []
word_list = ''

for char in s:
    if char.isdigit() == True :
        num_list.append(int(char))
    
    else:
        word_list += char

        if word_list in num_dict :
            num_list.append(num_dict[word_list])
            word_list = ''
        else:
            continue
        
for num in num_list:
    answer += str(num)

print(answer)