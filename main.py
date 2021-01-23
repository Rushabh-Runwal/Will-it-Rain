import os
from twilio.rest import Client
import requests


api_key = ''

account_sid = ''
auth_token = ''
my_phone_no = '+14155926492'

# Abad
# lat = 19.877552
# lon = 75.345026

# Pune
lat = 18.468599
lon = 73.834460



parameters = {
    'lat':lat,
    'lon':lon,
    'exclude': "current,minutely,daily",
    'appid':api_key,
}


fron_url  = requests.get(f'https://api.openweathermap.org/data/2.5/onecall',params=parameters)
data = [ i['weather'][0]['id'] for i in fron_url.json()['hourly'][:12] ]

if any([True for i in data if i<800]):
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It Will Rain so don't forget to take a umbrella with you.",
        from_=my_phone_no,
        to='+91 7447312272' # that's my no.
    )

    print(message.sid)