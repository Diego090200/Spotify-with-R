import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


#  Authentication
cid = "c2f4d1147b804b468423e1b9106665f2"
secret = "7b7e5ca5618f4cab9dc0ffcee131cbe6"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))

#  Scope
scope = "user-library-read"

#  Body of the code
artis_link = 'https://open.spotify.com/artist/0GWCNkPi54upO9WLlwjAHd?si=eYYENqfMQIi2VnaP8v1hhQ'
results = spotify.artist_albums(artis_link, album_type='album')
albums = results['items']
album_uri = []
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print("Nombre: ", album['name'], )
    if len(album_uri) <= 0:
        album_uri.append(album["uri"])
    else:
        contador = 0
        for i in album_uri:
            if i == album["uri"]:
                contador+1
        if contador == 0:
            album_uri.append(album["uri"])
album_json = json.dumps(albums[0])
pprint.pp(album_json)
print("\n")
#  Body of the code for the tracks
results = spotify.album_tracks(album_uri[0], offset=0)
tracks = results['items']
print("antes del while")
while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])
print("despues del while")
for track in tracks:
    print("Nombre de la canción: ", track['name'])
track_json = json.dumps(tracks[0])
pprint.pp(track_json)
print("\n")
# body of the code for top 10 tracks
artis_link = 'https://open.spotify.com/artist/0GWCNkPi54upO9WLlwjAHd?si=eYYENqfMQIi2VnaP8v1hhQ'
results2 = spotify.artist_top_tracks(artis_link)
canciones = results2["tracks"]
contador2 = 0
for cancion in canciones:
    print(f"###{contador2}###")
    print(cancion)
    data = json.dumps(cancion)
    pprint.pp(data)
    contador2 = contador2 + 1
