f = open("hello.dat", "w", encoding="utf-8")
for i in range(5):
    f.write("你好!!\n")
f.close()