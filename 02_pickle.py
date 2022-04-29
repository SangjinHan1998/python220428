# save python object as pickle
import pickle


data = {     
    "goal1" : "Push - up 100 times everyday",
    "goal2" : "Programming 12 hour everyday"     
}

file = open("./fastcampus1/chapter10파일입출력/data1.pickle", "wb") 
pickle.dump(data, file)
file.close

# 2. bring pickle file to Python
file = open("./fastcampus1/chapter10파일입출력/data1.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()