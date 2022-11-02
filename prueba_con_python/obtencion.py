import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


class Obtencion:
    def __init__(self, cliente_id: str, cliente_secreto: str):
        self.cid = cliente_id
        self.secret = cliente_secreto
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=self.cid, client_secret=self.secret))

    def obtener_albumes(self, artist_link: str):  # retorna los json de cada album
        results = self.spotify.artist_albums(artist_link, album_type='album')
        albums = results['items']
        while results['next']:
            results = self.spotify.next(results)
            albums.extend(results['items'])
        albumes_json = []
        for album in albums:
            album_json = json.dumps(album)
            albumes_json.append(album_json)
        return albumes_json

    def obtener_tracks(self, album_uri):  # obtiene los json de cada una de las canciones en un album
        results = self.spotify.album_tracks(album_uri, offset=0)
        tracks = results['items']
        while results['next']:
            results = self.spotify.next(results)
            tracks.extend(results['items'])
        tracks_json = []
        for track in tracks:
            track_json = json.dumps(track)
            tracks_json.append(track_json)
        return tracks_json

    def obtener_top(self, artist_link):  # obtiene toda la info del top 10 de canciones
        # y los devuelve en una lista de json
        results2 = self.spotify.artist_top_tracks(artist_link)
        canciones = results2["tracks"]
        top = []
        for cancion in canciones:
            data = json.dumps(cancion)
            top.append(data)
        return top
