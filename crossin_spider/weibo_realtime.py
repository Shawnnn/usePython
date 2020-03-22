import requests as req

url ='https://weibo.com/a/hot/realtime'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
'cookie':'SINAGLOBAL=2036369407374.6143.1508662473971; SCF=AqqdQXNIsVta13puF0BSphY38gwFdzFBe8_C8Nlkj7UrHyauVQcywMGyR7qJFBUAdJyTgRlTyHQUqSkRz9tMezk.; SUHB=0cS249AAit3ilX; _s_tentry=mcar.co; UOR=mcar.co,widget.weibo.com,mcar.co; Apache=1892693015691.7576.1582989914146; ULV=1582989914179:1:1:1:1892693015691.7576.1582989914146:; Ugrow-G0=cf25a00b541269674d0feadd72dce35f; SUB=_2AkMpK_7jf8NxqwJRmP0dy2zgaY1yyA3EieKfdw84JRMxHRl-yT92qlQftRB6AqvQDM4laN_hVVZUHv7oz2bFqlJKSWzo; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhHOwz2RrsLK5f945ZS6l4n; TC-V5-G0=595b7637c272b28fccec3e9d529f251a; WBStorage=42212210b087ca50|undefined'
}
res = req.get(url, headers = headers)
print('encoding:\t',res.encoding)
print('res.text:\n',res.text)
with open('./assets/weibo_realtime.html', "w", encoding = res.encoding) as f:
    f.write(res.text)
    print('html save succeeded!\n')
