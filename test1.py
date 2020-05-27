import random
my = int(input("請決定 [0]棒 [1]老虎 [2]雞 [3]蟲子:  "))
pc = random.randint(0,3)

trans = ["棒","老虎", "雞","蟲子"]

print("我出", trans[my])
print("電腦", trans[pc])

if my == (pc+1)%4:
    print("我輸")
elif pc == (my+1)%4:
    print("我贏")
else:
    print("平手")