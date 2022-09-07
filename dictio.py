txt_file = open("ruswords2.txt", encoding='utf-8', mode="r")
file_content = txt_file.read().lower()
content_list = file_content.split("\n")
txt_file.close()
word_number = 0
count = 1
while word_number <= len(content_list)-1:
    word = content_list[word_number]
    word_reverse = word[::-1]
    if word == word_reverse and len(word) >= 3:
        print(count, word)
        word_number += 1
        count += 1
    else:
        word_number += 1


