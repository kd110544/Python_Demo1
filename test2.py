import random
low = 1
high = 100
ans = random.randint(low,high)

while True:
    i = int(input("請輸入"+str(low)+"到"+str(high)+"範圍內的數字: "))
    if i == ans:
        print("你猜對了")
        break
    elif i < ans:
        print("再大一點")
        low = i
    elif i > ans:
        print("再小一點")
        high = i
