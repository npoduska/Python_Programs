"""This program sends SMS stock alerts.
Whenever the stock moves more than 5%, an alert is sent, along with a few news clips about the stock."""


import requests
from config import API_KEY, NEWS_API_KEY,ACCOUNT_SID, AUTH_TOKEN,FROM_NUMBER,TO_NUMBER #Get your own API Keys!
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Ares Capital Corporation"
# COMPANY_NAME = "Boeing"

#Twilio account access stuff
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY}'
r = requests.get(url)
stock_data = r.json()

close_prices =[]  #Initialize an array
opening_prices =[]  #Initialize an array

# Iterate over the list, collecting the bits of data we really want
for date, values in stock_data['Time Series (Daily)'].items():
    opening_prices.append(float(values['1. open']))
    close_prices.append(float(values['4. close']))

yesterday_close_price = int(close_prices[0])
day_before_yesterday_open_price = int(opening_prices[1])

# print(stock_data['Time Series (Daily)'][yesterday_date]['1. open'])
# yesterday_open_price = stock_data['Time Series (Daily)'][yesterday_date]['1. open']   


# day_before_yesterday_open_price = stock_data['Time Series (Daily)'][day_before_yesterday]['1. open']    
print(f" Yesterday's close price: ${yesterday_close_price:.2f}")
print(f" The day before yesterday's opening price: ${day_before_yesterday_open_price:.2f}")
# Two numbers to compare
num1 = float(yesterday_close_price)
num2 = float(day_before_yesterday_open_price)
# num2=28  #Testing purposes only

# print(num1, num2)
# Calculate the percentage difference
percentage_difference = abs(num1 - num2) / ((num1 + num2) / 2) * 100

print(f"The percentage difference for {COMPANY_NAME} is {percentage_difference:.2f}%")

if percentage_difference > 5:
    print("GET NEWS!")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body= f"The percentage difference for {COMPANY_NAME} is {percentage_difference:.2f}%",
    from_=f"{FROM_NUMBER}",
    to=f"{TO_NUMBER}",)
    
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    news_url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2024-09-13&sortBy=popularity&apiKey={NEWS_API_KEY}'

    response = requests.get(news_url)
    data = response.json()  # Call the method
    print(data['totalResults']) 
    if 0 < int(data['totalResults']): 
        if int(data['totalResults']) >5:
            max_articles = 4
        for i in range (0, max_articles):
            print(data['articles'][i]["source"]['name']) #Get where the article came from.
            print(data['articles'][i]["title"])    # This will print the parsed JSON data, particularly the title portion
            print(data['articles'][i]["description"])    # This will print the parsed JSON data, particularly the description portion
            # print(data) 
            #Send the news out via Twilio SMS
            news_source = (data['articles'][i]["source"]['name']) #Get where the article came from.
            news_title = (data['articles'][i]["title"])    # This will print the parsed JSON data, particularly the title portion
            news_description = (data['articles'][i]["description"])   
            
            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body= f"News source: {news_source}, Title: {news_title}, Desciption: {news_description}",
            from_=f"{FROM_NUMBER}",
            to=f"{TO_NUMBER}",)
    else:
        print(f"There are no news articles found for {COMPANY_NAME}.")  
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body= f"There are no news articles found for {COMPANY_NAME}.",
        from_=f"{FROM_NUMBER}",
        to=f"{TO_NUMBER}",)   


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 





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

