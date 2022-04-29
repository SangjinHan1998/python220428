# my explanation process
import csv

stock = [
    ["company", "purchase_price", "amount", "goal_price"],
    ["Samsung", 85000, 10, 90000],
    ["Naver", 380000, 5, 400000],
    ["HDC", 12300, 140, 18900]

]

file = open("./fastcampus1/chapter10파일입출력/stock.csv", "w",  newline="", encoding = "utf-8-sig")
writer = csv.writer(file)

for d in stock:
    writer.writerow(d)


file.close() 
