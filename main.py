STOCK = "APPLE"
COMPANY_NAME = "Apple"
NEWS_API_KEY = "YOUR-API-KEY"
ALPHAVANTAGE_API_KEY = "YOUR-API-KEY"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = 'YOUR-ACC-SID'
auth_token = "YOUR-AUTH-TOKEN"
from datetime import datetime
import requests
from twilio.rest import Client

# print(datetime.now().day)
from datetime import datetime, timedelta

# Get today's date
today = datetime.now().date()

# Calculate yesterday's date
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)
print("Yesterday's date:", yesterday)
print("day_before_yesterday:", day_before_yesterday)

parameters={"function": "TIME_SERIES_DAILY"
              ,"apikey": NEWS_API_KEY
              ,"outputsize": "compact"
              ,"symbol": STOCK}

price_request= requests.get(url = 'https://www.alphavantage.co/query', params=parameters)
data=price_request.json()
print(data)
yesterday_close = price_request.json()['Time Series (Daily)'][f'{yesterday}']['4. close']
day_before_yesterday_close=price_request.json()['Time Series (Daily)'][f'{day_before_yesterday}']['4. close']
print(yesterday_close)
print(day_before_yesterday_close)
print(data)
percentage_change=(float(yesterday_close) - float(day_before_yesterday_close)) /float(yesterday_close)
print(percentage_change)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
url = ('https://newsapi.org/v2/everything?'
       f'q={STOCK}&'
       'from=2024-06-044&'
       'sortBy=popularity&'
       'apiKey=bd441fa4e8c54cadbd81e6925b5c662f')

r= requests.get(url)
title=r.json()['articles'][0]['title']
brief=r.json()['articles'][0]['description']
url=r.json()['articles'][0]['url']
print(r.json())
print(r.json()['articles'][0]['title'])
print(r.json()['articles'][0]['description'])
print(r.json()['articles'][0]['url'])


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

client = Client(account_sid, auth_token)
message = client.messages.create(
        from_='+12087470851',
        body=f' 🔺 {COMPANY_NAME} \n '
             f'Headline: {title}\n'
             f'Brief: {brief}\n'
             f'For further details visit {url}\n',
        to='+919354632052'
    )

print(message.status)
print(message.sid)



