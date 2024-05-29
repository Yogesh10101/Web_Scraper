import requests
from plyer import notification
from apischeduler.schedulers.blocking import BlockingScheduler
import pytz

header = {
    'Authorization': 'Bearer 6a302705-a7da-462d-b801-f9f5ce7c1a57',
    'Content-Type': 'application/json'
}

response = requests.get("https://api.brightdata.com/dca/dataset?id=j_lc534zsd10y7bcu5f0", headers=headers)


prices = []
for obj in response.json():
    prices.append(obj['price'])

scheduler = BlockingScheduler()

tz = pytz.timezone('Europe/London')

def send_notification():
    for price in prices:
        if price < 300:
            notification.notify(
                title='Price Alert',
                message='The price is under 300!', 
                timeout = 10
        )

scheduler.add_job(send_notification,'cron', hour=10, minute=6, timezone=tz)

scheduler.start()