import requests
import time
from bs4 import BeautifulSoup
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nkust1112web56.settings')
django.setup()
from mysite import models

models.NKUSTnews.objects.all().delete()
urls = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
for page in range(1, 54):
    url = urls.format(page)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
    titles = soup.select(sel)
    for title in titles:
        new_rec = models.NKUSTnews(title=title.text.strip())
        new_rec.save()
    time.sleep(3)                 #這是每一頁讀取之間的間隔，絕對不能省略
    print("page:{}".format(page))
print("Done!")