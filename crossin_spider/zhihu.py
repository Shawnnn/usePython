import requests as req
import time
import pandas as pd

count =2
id = 5
list_dic = []
while count<6:
    url =f'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=fa69eff3daac0a02a25e154d7142a5e2&desktop=true&page_number={count}&limit=6&action=down&after_id={id}&ad_interval=-1'
    headers = {'cookie':'d_c0="AGACZDhtaQyPTqx74G-1-5m-vPAKB3NQcbA=|1506013492"; _zap=d76ac55d-7dbe-4467-8835-13d48cf0f3fb; _xsrf=849d4048-fe26-41bb-9e2e-9548ff103ddd; l_n_c=1; n_c=1; z_c0=Mi4xMGc0cEFBQUFBQUFBWUFKa09HMXBEQmNBQUFCaEFsVk41S3MxWHdDYTMtcTZrX2twR1QwNTZQelQ0TnlOdjFrV293|1581800932|9641c8907864cc610bb25fd62581207ce2baff3b; tst=r; oauth_from="/settings/account"; q_c1=03adec5f2efd4f7a844942b25a3650dc|1582402587000|1506013491000; __utma=51854390.312103905.1582402691.1582402691.1582402691.1; __utmc=51854390; __utmz=51854390.1582402691.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/20923466/top-answers; __utmv=51854390.100-1|2=registration_date=20131217=1^3=entry_date=20131217=1; _ga=GA1.2.312103905.1582402691; _gid=GA1.2.912505582.1584737924; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1584876194,1584881098,1584883223,1584888603; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1584888603; KLBRSID=e42bab774ac0012482937540873c03cf|1584888969|1584888600; _gat_gtag_UA_149949619_1=1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    time.sleep(0.2)
    res = req.get(url, headers = headers)
    print(f'get one news!\t page_number:{count};\t id:{id}')
    count += 1
    id += 6
    
    #print('res.status_code:\t',res.status_code)
    #print('res.encoding:\n',res.encoding)
    #print('res.json():\n', res.json())
    dic ={} # id, target/type, target/question/title

    for item in res.json().get('data'):
        dic['id'] = item.get('id')
        dic['type'] = item.get('target').get('type')
        if item.get('target').get('type') == "answer":
            #
            dic['title'] = item.get('target').get('question').get('title')
        elif item.get('target').get('type') == "article":
            dic['title'] = item.get('target').get('title')
    
    list_dic.append(dic)
print('list_dic:\n',list_dic)

df = pd.DataFrame(list_dic)
# writer = pd.ExcelWriter('./assets/zhihu.csv', engine = 'xlwt')
# writer.save()
df.to_csv('./assets/zhihu.csv', sep=';', encoding='gbk') # 含中文，需要用gbk 编码，utf-8会乱码
