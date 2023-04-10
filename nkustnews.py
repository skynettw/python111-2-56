import requests
import time
from bs4 import BeautifulSoup
urls = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
for page in range(1, 54):
    url = urls.format(page)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
    titles = soup.select(sel)
    for title in titles:
        print(title.text.strip())
    time.sleep(3)                 #這是每一頁讀取之間的間隔，絕對不能省略