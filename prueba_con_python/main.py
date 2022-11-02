import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


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
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
