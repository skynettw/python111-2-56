f = open("bodyinfo.txt", "r", encoding="utf-8")
rawdata = f.readlines()
f.close()

data = [item.split(",") for item in rawdata]
heights = [int(d[1]) for d in data]
#heights = [int(d['height']) for d in data]  <== 可讀性較高 (字典索引)
weights = [int(d[2]) for d in data]
bmis = [ round(int(d[2]) / (int(d[1])/100)**2,2) for d in data]
'''
bmis = list()
for d in data:
    w = int(d[2])
    h = int(d[1])
    bmi = w / h **2 
    bmis.append(bmi)
'''
print("本班最高是{}公分！".format(max(heights)))
print("本班最矮是{}公分！".format(min(heights)))
print("本班平均身高是{}公分！".format(sum(heights)/len(heights)))
print("本班的平均BMI是{}".format(sum(bmis)/len(bmis)))