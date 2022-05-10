from unicodedata import category
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup

url = 'https://www.hcpcsdata.com/Codes'


hcpcs = []
long_description = []
code = []
category = []
short_Description = []
tables = pd.read_html(url)

for i in tables[0]['HCPCS Codes']:
    hcpcs.append(i)

for k in hcpcs:
    url1 = 'https://www.hcpcsdata.com/Codes/' + k[1]
    data = requests.get(url1)

    html = soup(data.text, 'html.parser')

    tables = pd.read_html(url1)
    for i in tables[0]['Description']:
        long_description.append(i)
    for i in tables[0]['Code']:
        code.append(i)
        url2 = 'https://www.hcpcsdata.com/Codes/' + k[1] +  '/' + i #Short Description
        tables1 = pd.read_html(url2)
        for i in tables1[0]:
            short_Description.append(i)


# print(hcpcs)
dict = {'Group': hcpcs,'Code' : code, 'long_description': long_description, 'Short Description' : short_Description}        

df = pd.DataFrame(dict) 

df.to_csv('GFG.csv') 
