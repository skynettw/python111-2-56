f = open("bodyinfo.txt", "r", encoding="utf-8")
rawdata = f.readlines()
f.close()
for item in rawdata:
    name, h, w = item.split(",")
    bmi = int(w.strip()) / (int(h.strip())/100)**2
    print(name.strip(), round(bmi,2))