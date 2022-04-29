import csv 

file = open("./fastcampus1/chapter10파일입출력/student.csv", "r",  newline="", encoding = "utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()