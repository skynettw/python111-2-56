from django.shortcuts import render
from django.http import HttpResponse
import requests, json

def index(request):
    myname = "金城武"
    return render(request, "index.html", locals())

def all(request):
    url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"
    r = requests.get(url)
    data = json.loads(r.text)
    msg = ""
    msg = "<h2>" + data["updated_at"] + "</h2><br>"
    bicycle_data = data["retVal"]
    msg = msg + "<table><tr><td>站名</td><td>自行車數量</td></tr>"
    for item in bicycle_data:
        msg = msg + "<tr bgcolor=#ccffcc><td>{}</td><td>{}/{}</td></tr>".format(
            item['sna'].split("_")[1], 
            item['sbi'], 
            item['tot'])
    msg = msg + "</table>"
    return HttpResponse(msg)
