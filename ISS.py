import urllib.parse
import requests
import json
from datetime import datetime

while True:
    location = input('Enter location name : ')  # Bangkok, Washington
    if location[0] == '/':
        location = location[1::].capitalize()
        # print(location)
        # latitude & Longitude
        key = 'AdZMk2iGUcusFQipU2yQoqhdJwSXkW3g'
        url_geo = 'https://www.mapquestapi.com/geocoding/v1/address?'
        url = url_geo + urllib.parse.urlencode({'key': key, 'location': location})
        res = requests.get(url)
        result = res.json()
        # print(result)
        latitude = result['results'][0]['locations'][0]['latLng']['lat']
        longitude = result['results'][0]['locations'][0]['latLng']['lng']
        # print(latitude)
        # print(longitude)

        # ISS  Pass Times
        url_isspass = 'http://api.open-notify.org/iss-pass.json?'
        url = url_isspass + urllib.parse.urlencode({'lat': latitude, 'lon': longitude})
        res = requests.get(url)
        result = res.json()
        # print(result)
        risetime_pass = result['response'][0]['risetime']
        # print(risetime_pass)


        message1 = location + ' is located at Latitude : ' + str(latitude) + ' and Longtitude : ' + str(longitude)
        # print(message1)

        message2 = 'In ' + location + ' the ISS will pass ' + datetime.fromtimestamp(risetime_pass).strftime('%A, %B %d, %Y %I:%M:%S')
        # print(message2)

        # Webex
        access_token = 'ODE0MWFkMDAtYzk3OC00N2E1LWIxM2YtNzIwNGE5YjBkNzE5MWVhNTE2YjEtZjZj_PF84_consumer'
        room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3'
        url = 'https://webexapis.com/v1/messages'
        message = message1 + '\n' + message2
        # message = 'Hello' + str(lati_longi['lat'])
        url = 'https://webexapis.com/v1/messages'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'markdown': message}
        res = requests.post(url, headers=headers, json=params)
    else:
        break
