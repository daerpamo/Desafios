setwd("")
datos<-read.csv("140810.csv")
View(datos)
Patron<-datos[datos$Patron==1:9,]
Patron[,-1]
Patrones<-Patron[,-1]
Patrones

str(Patrones)

matriz<-as.matrix(Patrones)
Promedios<-apply(matriz,1,mean, na.rm=T)
Promedios
Pat<-1:8
plot(Promedios~Pat)
regresion<-lm(Promedios~Pat)
regresion
abline(regresion, col=2)
summary(regresion)
