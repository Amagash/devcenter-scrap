import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from urllib.request import urlopen

def getdata(url):
    page = requests.get(url)
    return page.text

def get_links(url):
    raw_html = getdata(url)
    soup = BeautifulSoup(raw_html, 'html.parser')
    # links = [link.get('href') for link in soup.find_all('a', href=True)]
    # print(links)
    list_links = []
    for link in soup.find_all("a", href=True):
        
        # Append to list if new link contains original link
        if str(link["href"]).startswith((str(url))):
            list_links.append(link["href"])
            
        # Include all href that do not start with website link but with "/"
        if str(link["href"]).startswith("/"):
            if link["href"] not in dict_href_links:
                print(link["href"])
                dict_href_links[link["href"]] = None
                link_with_www = url + link["href"][1:]
                print("adjusted link =", link_with_www)
                list_links.append(link_with_www)
                
    # Convert list of links to dictionary and define keys as the links and the values as "Not-checked"
    dict_links = dict.fromkeys(list_links, "Not-checked")
    print(dict_links)



# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# print(soup.get_text().replace("\n", " "))
 
if __name__ == "__main__":

    url = "https://aws.amazon.com/tutorials/create-banking-bot-on-amazon-lex-v2-console/" 
    dict_href_links = {}
    get_links(url)
