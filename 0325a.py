import requests
import json
url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"

r = requests.get(url)
data = json.loads(r.text)
print(data["updated_at"])
bicycle_data = data["retVal"]
for item in bicycle_data:
    print("{}:{}/{}".format(
        item['sna'].split("_")[1], 
        item['sbi'], 
        item['tot']))