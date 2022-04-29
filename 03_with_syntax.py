# Using with syntax, Automatically file close

with open("./fastcampus1/chapter10파일입출력/data1.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)
    