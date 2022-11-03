
#Libreria para graficar
library(ggplot2)
#Obtener nombres de col
names(tops_mongo)
# Definir rangos
range(tops_mongo$name)
range(tops_mongo$popularity)
#Crear Grafica
ggplot(tops_mongo, aes(x=name, y=popularity)) + geom_bar(stat = "identity")
