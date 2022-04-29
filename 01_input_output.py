# 1. file write
file = open("data.txt", "w", encoding = "utf8")    
# course -> make txt.file in current open folder
# encoding = "utf8" --> apply languaged
# ./fastcampus1/chapter10파일입출력/data.txt" --> set disired folder path
file.write("1. Study-Python-Developer-chapter10_File_input_output txt 파일을 만들었다!!")
file.close()


# 2. file add
file = open("./fastcampus1/chapter10파일입출력/data.txt", "a", encoding="utf8")
# a (subsequent writing)
file.write("\n2. I must have a job in 2022.")
file.close()

# 3. file read
file = open("./fastcampus1/chapter10파일입출력/data.txt", "r", encoding="utf8")

# 3.1 read file entire
#data = file.read()
#print(data)    
#file.close() 


# 3.2 read file one line
while True:
    data = file.readline()
    print(data,end="")
    if data == "":
        break
file.close()