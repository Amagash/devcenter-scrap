import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from urllib.request import urlopen

def getdata(url):
    page = requests.get(url)
    return page.text


# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# print(soup.get_text().replace("\n", " "))
 
if __name__ == "__main__":

    url = "https://aws.amazon.com/tutorials/create-banking-bot-on-amazon-lex-v2-console/" 
    print(getdata(url))