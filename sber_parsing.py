from bs4 import BeautifulSoup
import pandas as pd
import os

file_name = os.path.join('C:/Users/volla/Downloads/test.html')
print(file_name)
file_handle = open(file_name, encoding='utf-8')

soup = BeautifulSoup(file_handle, features='lxml')

b_trs = soup.find('div', {'class': 'b-trs'})
old_b_trs = b_trs.find_all(class_='trs_it')
parse_name = []
parse_date = []
parse_sum_trs = []
for i in old_b_trs:
    # print(i)
    name = i.find(class_='trs_name').text
    name = name.strip()
    date = i.find(class_='idate').attrs['data-date']
    q = i.find(class_='trs_st-refill')
    sum_trs = i.find(class_='trs_sum-am').parent.text.strip()
    sum_trs = sum_trs.replace(",", ".")
    sum_trs = float(''.join([i for i in sum_trs if i.isdigit() or i == '.']))
    if q:
        sum_trs = -sum_trs
    print(sum_trs)
    parse_name.append(name)
    parse_date.append(date)
    parse_sum_trs.append(sum_trs)
df = pd.DataFrame({'name':parse_name, 'date':parse_date, 'sum':parse_sum_trs})
df.to_excel(r'C:\Users\volla\Downloads\mydata.xlsx')
