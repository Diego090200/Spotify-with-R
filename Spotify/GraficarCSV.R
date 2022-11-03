install.packages("ggplot2")
install.packages("ggplot")
install.packages("tidyverse")

#Libreria para graficar
library(ggplot2)
#Obtener nombres de col
names(top_csv)
# Definir rangos
range(top_csv$name)
range(top_csv$popularity)
#Crear Grafica
ggplot(top_csv, aes(x=name, y=popularity)) + geom_bar(stat = "identity")
