txt_file = open("dictionary.txt", "r")
file_content = txt_file.read()
# print("The file content are: ", file_content)

content_list = file_content.split("\n")
txt_file.close()
word_number = 0
a=0
print(len(content_list))
while a<= len(content_list):
    if content_list[word_number]==content_list[word_number::-1]:
        print(content_list[word_number])
    else:
        print("не нашел в", content_list[word_number])
        a+=1
        word_number+=1

