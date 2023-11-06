import requests 
import json
import re
import boto3
from bs4 import BeautifulSoup
from tqdm import tqdm

def upload_to_s3(product_name):
    s3 = boto3.client('s3')
    s3.upload_file(f"{product_name}_desc.html", "knowledge-base-aws-products", f"{product_name}_desc.html")
    s3.upload_file(f"{product_name}_faq.html", "knowledge-base-aws-products", f"{product_name}_faq.html")

def create_file(product_name, url, content):
    f = open(f"{product_name}_{content}.html", "w")
    f.write(requests.get(url).text)
    f.close()

def get_data(url):
    data = []
    raw_data = requests.get(url).json()
    for item in tqdm(raw_data["items"]):
        product_url = item["item"]["additionalFields"]["productUrl"]
        product_name = item["item"]["name"]
        product_faq = product_url.replace('?did=ap_card&trk=ap_card', 'faqs')
        create_file(product_name, product_url, "desc")
        create_file(product_name, product_faq, "faq")
        upload_to_s3(product_name)

if __name__ == "__main__":

    url = "https://aws.amazon.com/api/dirs/items/search?item.directoryId=aws-products&sort_by=item.additionalFields.productNameLowercase&sort_order=asc&size=300&item.locale=en_US&tags.id=aws-products%23type%23service&tags.id=!aws-products%23type%23variant"
    get_data(url)