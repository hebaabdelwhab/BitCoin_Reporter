import requests
import time

# Info of Connection
api_Key = '84acfa59-0c9d-4478-8953-401443d71993'
bot_Key = '5330549188:AAEjS0935gbnIUA8H9C9srQL5AqKwCrrIdM'
chat_ID = '5298363419'
limit = 59000
time_Interval = 5

def getPrice():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': api_Key,
    }
    response = requests.get(url, headers=headers).json()
    btc_Price = response['data'][0]['quote']['USD']['price']
    return btc_Price

def send_Updates(chat_id, msg):
    url = f'https://api.telegram.org/bot{bot_Key}/sendMessage?chat_id={chat_id}&text={msg}'
    requests.get(url)

def main():
    while True:
        price = getPrice()
        if price<limit:
           send_Updates(chat_ID,f"BitCoin price is {price}")
        time.sleep(time_Interval)

main()


