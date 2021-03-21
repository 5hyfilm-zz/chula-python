str1 = 'Shane likes football; he is a big fan of Arsenal football team.'
str2 = ''.join(e for e in str1 if (e.isalnum() or e.isspace()))
str3 = str2.lower()

def fhash(word, M, G=37):
    sum_ord_num = 0
    for letter in word:
        ord_num = ord(letter)
        sum_ord_num += ord_num*(G**M)
        result = sum_ord_num%M
    return result

word_list = []
for word in str3.split():
    # print(word)
    word_list.append(word)

for word in word_list:
    f_word = fhash(word, 4)
    # print(f_word)
    print(word, f_word)
    
#     for letter in word:
#         print(letter)

