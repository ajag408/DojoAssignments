word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
for string in word_list:
    for character in string:
        if character == char:
            new_list.append(string)


print new_list
