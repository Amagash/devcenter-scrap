from bs4 import BeautifulSoup
import requests 
from urllib.request import urlopen
url = "https://aws.amazon.com/tutorials/create-banking-bot-on-amazon-lex-v2-console/" 

page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text().replace("\n", " "))
 
# payload = { 
# 	"uname": "test", 
# 	"pass": "test" 
# } 
# s = requests.session() 
# response = s.post(URL, data=payload) 
# print(response.status_code) # If the request went Ok we usually get a 200 status. 
 
# from bs4 import BeautifulSoup 
# soup = BeautifulSoup(response.content, "html.parser") 
# protected_content = soup.find(attrs={"id": "pageName"}).text 
# print(protected_content)