import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import re


def get_data(url):
    data = []
    raw_data = requests.get(url).json()
    i=1
    for item in raw_data["items"][:3]:
        product_url = item["item"]["additionalFields"]["productUrl"]
        product_name = item["item"]["name"]
        product_faq = product_url.replace('?did=ap_card&trk=ap_card', 'faqs')
        f_product = open(f"{product_name}.html", "w")
        f_product.write(requests.get(product_url).text)
        f_product.close()
        f_faq = open(f"{product_name}_faq.html", "w")
        f_faq.write(requests.get(product_faq).text)
        f_faq.close()

        i+=1
        data.append({"product_name": product_name, "product_url": product_url, "product_faq": product_faq})
    print (data)
    return data


if __name__ == "__main__":

    url = "https://aws.amazon.com/api/dirs/items/search?item.directoryId=aws-products&sort_by=item.additionalFields.productNameLowercase&sort_order=asc&size=300&item.locale=en_US&tags.id=aws-products%23type%23service&tags.id=!aws-products%23type%23variant"
    get_data(url)