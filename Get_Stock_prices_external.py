import requests

from pprint import PrettyPrinter
pp = PrettyPrinter()
access_key='201ea7f73daef933f82bac8276ad2112'

# Get EOD Stock Data
url='http://api.marketstack.com/v1/eod'
params = {'access_key': access_key, 'symbols':'TSLA'}
api_result = requests.get(url, params)
api_response = api_result.json() 
#for i in api_response['data']:
    #print (i['date'], i['symbol'],i['open'],i['high'],i['low'],i['volume'])
    
    
# Get Intraday Stock Data
url='http://api.marketstack.com/v1/intraday'
params = {'access_key': access_key, 'symbols':'AAPL'}
api_result = requests.get(url, params)
api_response = api_result.json() 
#for i in api_response['data']:
 #print (i['date'], i['symbol'],i['open'],i['high'],i['low'],i['volume'])
    
    
# Get Historical Stock Data
url='http://api.marketstack.com/v1/intraday'
params = {'access_key': access_key, 'symbols':'AAPL', 'date_from': '2021-05-25','date_to': '2021-06-04'}
api_result = requests.get(url, params)
api_response = api_result.json() 
#for i in api_response['data']:
  #  print (i['date'], i['symbol'],i['open'],i['high'],i['low'],i['volume'])

# Get Real Time Updates
url='http://api.marketstack.com/v1/intraday'
params = {'access_key': access_key, 'symbols':'AAPL', 'interval': '1min'}
api_result = requests.get(url, params)
api_response = api_result.json() 
#print(api_response)
#for i in api_response['data']:
  #  print (i['date'], i['symbol'],i['open'],i['high'],i['low'],i['volume'])
    
#Get exchanges data
url='http://api.marketstack.com/v1/exchanges'
params = {'access_key': access_key}
api_result = requests.get(url, params)
api_response = api_result.json() 
#for i in api_response['data']:
  #print (i['name'], i['acronym'],i['mic'],i['country'],i['country_code'],i['city'],i['timezone'],i['currency'])

#Get currencies data
url='http://api.marketstack.com/v1/currencies'
params = {'access_key': access_key}
api_result = requests.get(url, params)
api_response = api_result.json() 
#for i in api_response['data']:
  #print (i['code'], i['symbol'],i['name']) 

#Get Timezones data
url='http://api.marketstack.com/v1/timezones'
params = {'access_key': access_key}
api_result = requests.get(url, params)
api_response = api_result.json() 
for i in api_response['data']:
  print (i['timezone'], i['abbr'],i['abbr_dst']) 