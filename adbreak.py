import requests
import json
 
data = {
  'grant_type': 'password',
  'client_id': '358fd6ea7fdec4e347e2',
  'client_secret': '1a746399d8881fcb49f37043daef057fcb7afdc9',
  'username': 'videocontent@audacy.com',
  'password': 'AudacyV!de0'
}
 #API KEY 358fd6ea7fdec4e347e2
 #API SECRET 1a746399d8881fcb49f37043daef057fcb7afdc9
response = requests.post('https://api.dailymotion.com/oauth/token', data=data)
json_data = json.loads(response.text)

print(json_data)
 
headers = {
    'Authorization': 'Bearer ' + json_data['access_token'],
}
 
data = {
  'live_ad_break_launch': '1'
}
 
response = requests.post('https://api.dailymotion.com/video/x8y77yq', headers=headers, data=data)
#betql=
#kdka=x8uaex4
json_data1 = json.loads(response.text)

print(json_data1)
#json_data1= json.loads(response.text)

