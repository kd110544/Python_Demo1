# 買到中?碼 需買幾張樂透彩
import random
prize = set()
while len(prize) < 7:
    prize.add(random.randint(1,48))
print("開獎號碼為: ", prize)

count = 0
while True:
    lottery = set()
    while len(lottery) < 7:
        lottery.add(random.randint(1,48))
    print("我買的樂透彩卷為: ", lottery)
    count = count + 1

    win = 0
    for n in lottery:
        if n in prize:
            print(n, "中了")
            win = win + 1
    print("總共中", win, "號碼")

    if win >= 4:
        print("總共買", count, "張樂透")
        break