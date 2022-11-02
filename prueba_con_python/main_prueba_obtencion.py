import pprint
import obtencion
import json


cid = "c2f4d1147b804b468423e1b9106665f2"
secret = "7b7e5ca5618f4cab9dc0ffcee131cbe6"
lista_artistas = ["https://open.spotify.com/artist/0GWCNkPi54upO9WLlwjAHd?si=eYYENqfMQIi2VnaP8v1hhQ",
                  "https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU?si=a44276415f51452f"]
funciones = obtencion.Obtencion(cid, secret)
cont_artista = 0
cont_album = 0
albumes_artistas_json = []
albumens_uris = []
#  aquí se agregarán todos los datos
for artista in lista_artistas:
    albumes_artistas_json.append(funciones.obtener_albumes(artista))
#  esto es solo para visualizar
for artista in albumes_artistas_json:
    print(f"\n#########       {cont_artista}       #########\n")
    for album in artista:
        print(f"\n################### {cont_album} ########################\n")
        pprint.pprint(album)
        cont_album += 1
        # Este paso es importante para poder leer la info de un json
        archivo_json = json.loads(album)
        albumens_uris.append(archivo_json["uri"])
    cont_artista += 1
print("\n\n")
#  En la variable albumes_uris vamos a tener el link para buscar las tracks de los albumes
print(albumens_uris)
