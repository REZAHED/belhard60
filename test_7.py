with open("input.txt", "r", encoding="utf-8") as file:
    letter = 0
    words = 0
    c=1
    for line in file:
       d = line.count(" ") + 1
       t=line.strip().replace(" ","").replace(",","").replace(".","")
       print(f"в {c} строке сущевствует {len(t)} букв" ,end=" ")
       print(f"в {c} строке сущевствует {d} слово")

       c+=1
