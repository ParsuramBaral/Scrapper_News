import requests
from bs4 import BeautifulSoup

def head_scrapper():
    beg = requests.get("https://kathmandupost.com/politics/")
    soup = BeautifulSoup(beg.content, "html.parser")
    trending_topics_list = soup.select(".trending-topics-list  a[href]")
    # list = []
    for link in trending_topics_list:
        print(f"{link["href"]}")

head_scrapper()



