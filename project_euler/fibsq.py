

f1 = 1
f2 = 1
count = 3
while True:
    c = str(f1 + f2)
    if len(c) == 1000:
        print(c, " the pos is :", count)
        break
    count +=1
    f1 = f2
    f2 = int(c)
