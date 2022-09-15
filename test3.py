text = input()
lst = list(text)
count = 0
i = 0

while i < len(lst)-1:
    if lst[i] == text[i+1]:
        count+=1
        i+=2
    else:
        i+=1
print(count)

# for i in range(0, len(lst)-1):
#     if lst[i] == lst[i+1]:
#         count += 1
# print(count)

