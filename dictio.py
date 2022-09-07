txt_file = open("dictionary.txt", "r")
file_content = txt_file.read()
# print("The file content are: ", file_content)

content_list = file_content.split("\n")
txt_file.close()
word_number = 0
a=0

while a<= len(content_list)-1:
    reverse = content_list[a]
    reverse2= reverse[::-1]
    if reverse==reverse2:
        print(reverse)
        a+=1
        # reverse = ""
        # reverse2 = ""
    else:
        a+=1
        reverse=""
        reverse2=""

