import requests as req 
from bs4 import BeautifulSoup as bf
import pandas as pd
import time

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'cookie':'lianjia_uuid=e0142bd1-6893-47a7-a663-3453150be621; lianjia_ssid=d89f80da-7ad7-459f-aef5-c80d18dd7e70; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNDc1ZGI5MTM4ZmE4OGM1MGFhMTY3OGQxNzdmNzI3Y2IyMDFlODhjZjhjZTkxZDIwMjY3NzJkODVkZDBjYTBjZjIwNzQ5NDRhZGM1ZWE2NGMyOWNjOWMwZjBlNmFkNWU4OGRhNGE0ZGM0N2QyOTFmOGYzZDRkODkwMmFkNjE0ZGM2MTNmMDE1ZWRkYmEyYmI2N2FiNWRjYjI1Y2QwNDhjMTBhNGYwNDYwYzFiNGRhNTA0ZjFiYTE2MWI5M2JkMTc4ZGNlYzExZDk5N2NiYWU4MDY4YTQzMGNiNWYxZGFjMmJkNTZkNGQ2ZTUzNDRiNzk1ZWI4ZWRjMTBmYjg5YjAyZWNkMzQ3NDEyMGI5YTExZjc3Y2U4ZTFlMTMwNmRmZmU4YmQxZjI3MmM0ZTllMGIwOGQ5ZTdjOGI5NDhmYjFhOWNkZmFlZTNkMzBkMmZjNjdkNDYwN2UzMTU2YjM3OWE2MVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJlMGQ1OGU0MFwifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL3p1ZmFuZy9wZzIvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='}
page = 1
dic_list = [] #列表字典，装要写入CSV的多个字典
erro_list = []
flag = True
while flag:
    time.sleep(0.5)
    res = req.get(f'https://sh.lianjia.com/zufang/pg{page}/', headers=headers)
    # print(res.text)
    html = res.text
    html_bf = bf(html, "lxml")
    # print(html_bf.prettify())

    results = html_bf.find_all('div', class_="content__list--item")

    #print('check results[0]:---------------------------\n',results[0],'\n-----------------------result end---------------------\n')
    count = 1
    url1 = 'https://sh.lianjia.com'
    for result in results:
        dic = {} # 保存一行数据
        print(f'loading page {page};\tdata {count}!\n')
        print('result\n',result)
        
        dic['title'] = result.a['title']
        dic['url'] =  url1 + result.a['href']

        loc_lst = []
        location = result.find('p', class_ = 'content__list--item--des') 
        for loc in location.find_all('a'):
            loc_lst.append(loc.get_text())
        dic['location'] = '-'.join(loc_lst)

        info = location.get_text(strip=True).split('/')
        if len(info) == 5:
            dic['area'] = info[1]
            dic['direction'] = info[2]
            dic['layout'] = info[3]
            dic['floor'] = info[4].replace(" ","")
        else:  # 粗略
            print(f"page {page}, data {count} is missing, info different!")
            erro_list.append(f"page {page}, data {count}")
            continue

        item_lst = [ item.get_text() for item in result.find('p', class_ = 'content__list--item--bottom oneline').find_all('i')]
        dic['others'] = ','.join(item_lst)

        dic['price'] = result.find('span', class_= 'content__list--item-price').get_text(strip=True)

        dic_list.append(dic) #保存一行数据
        print(f'\tpage {page}, data {count} is appended!\n----------------------\n')
        count +=1
    if page == 100:
        flag = False
    else:
        page += 1

print(f'total page {page}!')

# print(dic_list)

df = pd.DataFrame(dic_list)
# df.to_csv('./assets/lianjia.csv', sep='；', encoding = 'gbk', index =False)
writer = pd.ExcelWriter('./assets/lianjia.xlsx')
df.to_excel(writer, index = False)
writer.save()
print('saving  succeeded!\n')
print('below data are missing!\n',erro_list)
