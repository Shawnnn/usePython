import requests
while True:
    city = input('Please input a city name, input "Enter" to exit\n')
    if not city:
        print('exit!\n')
        break
    try:
        req = requests.get(f'http://wthrcdn.etouch.cn/weather_mini?city={city}')
    
    except:
        print('查询失败')
        break
    #print(f'type(req.text):{type(req.text)},\nreq.text:\n',req.text,'\n')
    
    dic_city = req.json() # json转化成字典
    print(f'type(dic_city):{type(dic_city)},\ndic_city:\n',dic_city,'\n')
    
    city_data = dic_city.get('data') # 读取字典中 键 data
    if city_data:
        city_forecast = city_data['forecast'][0]
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
