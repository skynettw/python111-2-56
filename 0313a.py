f = open("hello.dat", "w", encoding="utf-8")
for i in range(5):
    f.write("Hello world!!\n")
f.close()