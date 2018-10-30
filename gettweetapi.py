import requests

from bs4 import BeautifulSoup

url = "http://www.twitter.com/" #+username

response = requests.get(url)

html_icerik = response.content

soup = BeautifulSoup(html_icerik,"html.parser")

basliklar = soup.find_all("p",{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})

for baslik in basliklar:
    baslik = baslik.text

    baslik= baslik.strip()
    baslik = baslik.replace("\n","")
    print(baslik)
    
