import mysql.connector
import spotipy
from spotipy import SpotifyClientCredentials

sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
client_id='',
client_secret=''
))

database_config={
    'host':'localhost',
    'username':'root',
    'password':'Bothi@3',
    'database':'spotifyDb',
}

con=mysql.connector.connect(**database_config)
cursor=con.cursor();

with open('playlist.txt','r') as fi:
    urls=[file.strip() for file in fi if file.strip()]
track_data_list=list()

for url in urls:
    try:
        url=url.strip()
        track=sp.track(url)
        track_data={"track_name": track['name'],
                    "album_name": track['album']['name'],
                    "release_date": track['album']['release_date'],
                    "artists_name": track['artists'][0]['name'],
                    "popularity": track['popularity'],
                    "duration": track['duration_ms']/60000
                    }

        query="""insert into tracks(track_name,album_name,release_date,artists_name,popularity,duration_in_mins)
                values(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,
             (track_data['track_name'],
                     track_data['album_name'],
                     track_data['release_date'],
                     track_data['artists_name'],
                     track_data['popularity'],
                     track_data['duration']))
        print(f"{track_data['track_name']} is inserted into the database!")
        con.commit()

    except Exception as e:
        print(e)
con.close()
cursor.close()
fi.close()
