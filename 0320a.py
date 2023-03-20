f = open('data.txt', "a", encoding='utf-8')
d = int(input("d="))
while d >= 0:
    f.write(str(d)+"\n")
    d = int(input("d="))
f.close()