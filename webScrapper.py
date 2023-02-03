from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os

path = os.getenv('PATH');
print(path);
uins = ["16020013", "16020014", "16020015", "16020016", "16020017", "16020018"]
i = 1
dict_head = {'UID': [], 'Name': [], 'Rank': [], 'Unit': [], 'Gross Salary': [], 'Net Salary': []}
for uin in uins:
    driver = webdriver.Chrome()
    driver.get("https://ssb.gov.in/admnis/Employee/frmPaySlipPrint.aspx?UIN=" + uin + "&Month=august&Year=2022")
    content = driver.page_source
    print(content)
    driver.close()
    soup = BeautifulSoup(content, features="lxml")
    uid = soup.find('span', attrs={'id': 'lblPER_NO'})
    name = soup.find('span', attrs={'id': 'lblNAME'})
    rank = soup.find('span', attrs={'id': 'lblRANK'})
    unit = soup.find('span', attrs={'id': 'lblUnite_Desc'})
    gross_salary = soup.find('span', attrs={'id': 'lblgross_total'})
    net_salary = soup.find('span', attrs={'id': 'lblnet_amt'})
    dict_head["UID"].append(uid.text)
    dict_head["Name"].append(name.text)
    dict_head["Rank"].append(rank.text)
    dict_head["Unit"].append(unit.text)
    dict_head["Gross Salary"].append(gross_salary.text)
    dict_head["Net Salary"].append(net_salary.text)

df = pd.DataFrame(dict_head)
df.to_csv('product.csv', mode='a', index=False, encoding='utf-8')

# thisdict =	{
#   "brand": ["Ford"],
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["brand"].append("red")
# print(thisdict)
