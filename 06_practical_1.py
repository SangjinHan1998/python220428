# my explanation process
import csv

def show_profit(data):
    name = stock[0]   # company
    purchase_price = int(stock[1])
    amount = int(stock[2])
    goal_price = int(stock[3])

    profit = (goal_price - purchase_price) * amount
    profit_ratio = (goal_price / purchase_price -1) * 100

    print(f"{name} {profit} {profit_ratio:.2f}")    
    # :.2f 소수점 2번째자리까지만 출력

file = open("./fastcampus1/chapter10파일입출력/sto45ck.csv", "r",  newline="", encoding = "utf-8-sig")

reader = list(csv.reader(file))
for stock in reader[1:]:
    show_profit(stock)

file.close() 


"""
    '_csv.reader' object is not subscriptable
    This error is csv reader can't support indexing
    So cannot return csv.reader data.
"""