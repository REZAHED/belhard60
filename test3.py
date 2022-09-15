text = input()
lst = list(text)
count = 0
for i in range(0, len(lst)-1):
    if lst[i] == lst[i+1]:
        count += 1
print(count)

