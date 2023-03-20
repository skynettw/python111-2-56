import csv
filename = "bodyinfo.csv"
with open(filename, encoding='utf-8') as fp:
    dataread = csv.DictReader(fp)
    data = [dict(d) for d in dataread]
heights = [int(d['height']) for d in data]
print(heights)
