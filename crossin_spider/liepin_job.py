import requests as re 
from bs4 import BeautifulSoup 
import time
import pandas as pd 

def get_job(res, page): # 对当前页的所有搜索结果进行爬取
    soup = BeautifulSoup(res.text, 'lxml')
    items = soup.find_all('div', class_="sojob-item-main clearfix") # 定位到每个job 元素
    job_links = [] #构造空列表，存放当前页的所有结果
    for item in items:
        post = {} # 构造空字典，存放每个job的 page, job_title, job_link，job_description
        link = item.find('a').get('href')  # 获取这个job 的link
        if "liepin.com" not in link:
            link = "https://www.liepin.com" + link # 个别job 的link 是不全的，需要补全
        
        post['page'] = page
        post['job_title'] = item.find('h3').get('title')
        post['job_link'] = link

        job_links.append(post)
    # print(job_links)

    #获取job_description
    count = 1
    for post in job_links:
        time.sleep(2)
        job = re.get(post['job_link'], headers = headers)
        desc = BeautifulSoup(job.text, 'lxml')
        if "job-main job-description main-message" not in job.text:
            post['description'] = desc.find('div', class_ = "job-item main-message job-description").get_text(strip = True)
        else:
            post['description'] = desc.find('div', class_ = "job-main job-description main-message").get_text(strip = True)

        print(f'page {page}; count {count} is saving!')
        count += 1

    #写入
    df = pd.DataFrame(job_links)
    writer = pd.ExcelWriter('./assets/liepin_job.xlsx', mode = 'a')
    df.to_excel(writer, index = False, sheet_name='Sheet1')
    writer.save()
    
    # url = "https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=python"  # 普通url
page = 1

# 通过“下一页”的URL 构造可循环下一页的url
url = f"https://www.liepin.com/zhaopin/?init=-1&headckid=0ffd5d2c2f755568&fromSearchBtn=2&ckid=0ffd5d2c2f755568&degradeFlag=0&sfrom=click-pc_homepage-centre_searchbox-search_new&key=python&siTag=I-7rQ0e90mv8a37po7dV3Q%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId=8225b5022bf54f27b2a062bdae467ce7&d_curPage=3&d_pageSize=40&d_headId=8225b5022bf54f27b2a062bdae467ce7&curPage={page}"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'cookie':'__uuid=1585434932635.97; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1585434940; fe_se=-1585434968590; __tlog=1585434932636.14%7C00000000%7CR000000075%7C00000000%7C00000000; abtest=0; JSESSIONID=C7E96F6A23C842D96E08E3F8512191CB; __session_seq=5; __uv_seq=1; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1586725235'
}
while page < 4:
    time.sleep(2)
    res = re.get(url, headers = headers)
    get_job(res, page)
    # print(res.text)
    print(f'\n---------page {page} is done!-------------\n')
    page += 1
print('all are done!')
