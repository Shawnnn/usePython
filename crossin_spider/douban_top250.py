import requests as re
import time
import pandas as pd
from pathlib import Path
import csv

def request_url(url, headers={'user-agent':'chrome'}):
    rep = re.get(url,headers=headers)
    #print('encoding:\n', rep.encoding)
    print(f'read ok {url}!\n')
    return rep

'''
task 1 - get Shawshank Redemption image from douban
'''
url = "https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a"

rep = request_url(url)
print('get API response succeeded!\n')
result = rep.json()
print("result.json:\n",result)

img = rep.json().get('image')
img_rep = request_url(img)
print('get image response succeeded!\n')

with open('./douban_shawshank_img.jpg','wb') as f:
    f.write(img_rep.content)
    print('writing image succeeded!\n')

'''
taks 2 - get 250 movies info
'''
#获取包含多个电影的名为subjects的列表字典 "subjects":[...., ...., ....]

CWD = './assets'
p = Path(CWD)
start = 0
count = 0
total_list = []
flag = True #使用 布尔 flag来控制外部循环
while flag:
    time.sleep(0.2)
    url = f'https://api.douban.com/v2/movie/top250?start={start}&apikey=0df993c66c0c636e29ecbb5344252a4a'
    start += 1
    rep = request_url(url)
    top_res = rep.json()
    top_list = top_res.get("subjects")

    #获取所需内容，并构建一个列表字典
    for m in top_list:
        count += 1

        movie = {}
        movie['id'] = m.get('id')

        movie['title'] = m.get('title')

        casts_list = []
        for cast in m.get('casts'):
            casts_list.append(cast.get('name'))
        movie['casts'] = ','.join(casts_list)

        movie['img'] = m.get('images').get('small')

        total_list.append(movie)
        print(f"{count}: append movie {movie['title']} to the list!\n")

        #download post
        img_url = m.get('images').get('small')
        img_res = request_url(img_url)
        with open(p/f'{movie["title"]}_POST.jpg','wb') as f:
            f.write(img_res.content)
            print(f'\tdownload {movie["title"]} succeeded!\n')

        if count == 250:
            flag = False # 当count == 250 ，则停止外部循环（不再抓取新的API）
            break # 当count == 250 ，则停止内部循环（不再把当前剩余的列表放入字典中）

print(f'read {count} in total!\n')

print('total_list:\n',total_list)

#把列表字典写入csv

#按照pandas模块的方式
df = pd.DataFrame(total_list)
writer = pd.ExcelWriter(p/'douban_top250.csv', engine= 'xlwt') #构建一个writer
df.to_excel(writer) # df.to_excel 方法，输入writer
writer.save() #excel writer 保存

#按照 csv 模块的方式
# headers = ['id', 'title', 'casts', 'img']
# with open(p/'douban_top250.csv','w') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(total_list)
