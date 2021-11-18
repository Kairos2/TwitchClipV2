#global modules
import requests
import os

#my modules
import RFC3339 as kt
import streamer_id
import twitchloader as tl


#get autho token
client_id = 'gedxi171d6nb81wnfugrb5ss9g5w3f'
client_secret = 'h6xjgkch9rj3f8j4lhx0jo6f25mfst'

oauth_req = f'https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'

r1 = requests.post(oauth_req)
r1_json = r1.json()

Authorization = 'Bearer ' + r1_json['access_token']

######################################################################
current_streamer = 'lammysnax_'
######################################################################

b_id = streamer_id.streamer_id[current_streamer]


#get clips
head = {
        'Authorization': Authorization,
        'client-id': client_id
        }

clips_req = f'https://api.twitch.tv/helix/clips?broadcaster_id={b_id}&started_at={kt.start_time}&ended_at={kt.end_time}'

r2 = requests.get(clips_req, headers =head)
r2_json = r2.json()

#print(r2_json['data'][0]['url'])

os.chdir(f'/Users/keno/Desktop/twitch/{current_streamer}')

for i in range(len(r2_json['data'])):
        url = r2_json['data'][i]['url']
      #  views = r2_json['data'][i]['view_count']
      #  duration = r2_json['data'][i]['duration']
        tl.twitch_dl(url)
