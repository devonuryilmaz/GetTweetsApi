import requests

from bs4 import BeautifulSoup

url = "http://www.twitter.com/onuuryiilmaz"

response = requests.get(url)

html_icerik = response.content

soup = BeautifulSoup(html_icerik,"html.parser")

basliklar = soup.find_all("p",{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
i = 0

for baslik in basliklar:
    if i==50:
        break
    baslik = baslik.text

    baslik= baslik.strip()
    baslik = baslik.replace("\n","")
    print(baslik)
    i+=1