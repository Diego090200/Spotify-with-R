#Instalacion de packete para leer csv
install.packages("readr")
library(readr)
#Funcion para mostrar la ruta del csv
file.choose()
#Asignacion de la ruta a una variable
top <- "C:\\Users\\alehe\\Documents\\Trabajos\\10mo Ciclo\\Análisis de Datos\\Spotify-with-R\\prueba_con_python\\tops.csv"
#Guardar datos del csv en track_csv
top_csv <- read.csv(top)
#Mostrar DataFrame
head(top_csv)
