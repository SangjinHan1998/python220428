import csv  # internal module

data = [
    ["name", "class", "num"],
    ["Um",1, 4],
    ["Jun", 2, 12],
    ["Sik", 3, 3]

]

file = open("./fastcampus1/chapter10파일입출력/stu3333dent.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)
# newline -> Automatically write leaving space 
# utf-8-sig -> Not broken File

for d in data: 
    writer.writerow(d)
    # writerow -> Create each line of the list data csv.

file.close()