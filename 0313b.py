f = open("bodyinfo.txt", "a", encoding="utf-8")
name = input("姓名：")
while name!="":
    h = int(input("身高："))
    w = int(input("體重："))
    f.write("{},{},{}\n".format(name, h, w))
    name = input("姓名：")
f.close()