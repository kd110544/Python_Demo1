
f = open("f1.txt", "r", encoding="utf-8")
article = f.read()
f.close()

output = {}
for a in article:
    if not a in output:
        output[a] = 1  #加入dictionary
    else:
        output[a] = output[a] + 1  #修改值
print("數完的結果是:", output)
print("的出現次數為:", output["的"])
