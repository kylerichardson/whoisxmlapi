import json
import requests

BASE_URL = r'https://www.whoisxmlapi.com/whoisserver/WhoisService?outputFormat=JSON&domainName='

def get_whois(domain):
    response = requests.get(BASE_URL + domain)
    raw_data = response.json()

