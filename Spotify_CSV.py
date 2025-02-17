import spotipy
from spotipy import SpotifyClientCredentials
import pandas as pd
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
client_id='',
client_secret=''
))

with open('playlist.txt','r') as fi:
    urls = [i.strip() for i in fi if i.strip()]

track_data_list=list()
for url in urls:
    try:
        track_id = url.split("/")[-1].split("?")[0]
        track=sp.track(track_id)
        track_data={"track_name": track['name'],
                    "album_name": track['album']['name'],
                    "release_date": track['album']['release_date'],
                    "artists_name": track['artists'][0]['name'],
                    "popularity": track['popularity'],
                    "duration": track['duration_ms']/60000
                    }
        track_data_list.append(track_data)
    except Exception as e:
        print(e)
df = pd.DataFrame(track_data_list)
print(df)
df.to_csv("trackData.csv",index=False)