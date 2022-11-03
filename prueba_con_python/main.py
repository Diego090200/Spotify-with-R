import pprint
import obtencion
import json
import pandas as pd
import pickle
from database.db import Database
from database.mongodb import MongoConection


# variables para mongo
coneccion: Database = MongoConection()

# Variables de Spotify
cid = "c2f4d1147b804b468423e1b9106665f2"
secret = "7b7e5ca5618f4cab9dc0ffcee131cbe6"

# artistas
lista_artistas = ["https://open.spotify.com/artist/0GWCNkPi54upO9WLlwjAHd?si=eYYENqfMQIi2VnaP8v1hhQ",
                  "https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU?si=a44276415f51452f"]

# Variables a utilizar
funciones = obtencion.Obtencion(cid, secret)
cont_artista = 0
cont_album = 0
albumes_artistas_json = []  # Esta variable va a tener la info de los albumes
albumens_uris = []
tracks_info_json = []  # Esta va a tener la info de las tracks
top_tracks_info_json = []  # Esta del top 10, agrupada por artista (supongo)
#  Listas de json pero en diccionarios
albumens_dict = []
tracks_dict = []
top_dict = []


#  aquí se agregarán todos los datos
for artista in lista_artistas:
    albumes_artistas_json.append(funciones.obtener_albumes(artista))
    top_tracks_info_json.append(funciones.obtener_top(artista))
#  esto es solo para visualizar
for artista in albumes_artistas_json:
    print(f"\n#########       {cont_artista}       #########\n")
    for album in artista:
        print(f"\n################### {cont_album} ########################\n")
        pprint.pprint(album)
        cont_album += 1
        # Este paso es importante para poder leer la info de un json
        archivo_json = json.loads(album)
        albumens_dict.append(archivo_json)  # esto de aquí va a servir para guardar datos en mongo
        albumens_uris.append(archivo_json["uri"])
    cont_artista += 1
print("\n\n")
#  En la variable albumes_uris vamos a tener el link para buscar las tracks de los albumes
for uri in albumens_uris:
    tracks_info_json.append(funciones.obtener_tracks(uri))
    for lst_tr in top_tracks_info_json: # esto de aquí va a servir para guardar datos en mongo
        for tr in lst_tr:
            archivo_json = json.loads(tr)
            tracks_dict.append(archivo_json)

for artista in top_tracks_info_json:  # literal esto es para guardar datos en mongo
    for tr in artista:
        archivo_json = json.loads(tr)
        top_dict.append(archivo_json)

with open(r"C:\Users\alehe\Desktop\tops.json", 'w') as f:
    json.dump(top_dict, f)

top_csv = pd.read_json(r"C:\Users\alehe\Desktop\tops.json")
top_csv.to_csv('tops.csv')

# coneccion.insert(albumens_dict, "albumes")
# coneccion.insert(tracks_dict, "tracks")
coneccion.insert(top_dict, "tops")
