#Diseñar un programa que pida el total de kilómetros recorridos, el precio de la gasolina (por litro) 
#y el tiempo que se ha tardado (en horas y minutos) y que calcule:
#Consumo de gasolina (en litros y Bs.) en el recorrido.
#Velociad media (en km/h y m/s).
#Este vehículo ofrece un rendimiento promedio de 16 kilómetros por litro.


print("------------------------------------------------------------------")
print("Programa que calcula el consumo de combustible y la velocidad media")
print("------------------------------------------------------------------")



def Verificacion(a):
    intentos=1
    while(a<0):
        a=float(input("El valor no puede ser negativo, por favor ingrese valor positivo  "))
        if intentos==2:
                print("Has realizados muchos intentos")
                quit("El programa ha finalizado");
        if a<0:
                intentos=intentos+1
    if intentos<3:            
        return(a)       
    
        
Distancia_Recorrida=0
Precio_Gasolina=0
Tiempo_Recorrido=0
Rendimiemto=16

Distancia_Recorrida=float(input("Por favor ingrese la distancia recorrida en mts "))
Distancia_Recorrida=Verificacion(Distancia_Recorrida)

Tiempo_Recorrido=float(input("Por favor ingrese el tiempo recorrido en hrs  "))
Tiempo_Recorrido=Verificacion(Tiempo_Recorrido)

Precio_Gasolina=float(input("Por favor ingrese el precio de la gasolina en Bs. "))
Precio_Gasolina=Verificacion(Precio_Gasolina)


Consumo_gasolina=Distancia_Recorrida/Rendimiemto
Costo_gasolina=Consumo_gasolina*Precio_Gasolina
Velocidad_media_Kmh=Distancia_Recorrida/Tiempo_Recorrido
Velocidad_media_ms=(Distancia_Recorrida*1000)/(Tiempo_Recorrido*3600)

print(f"El consumo de gasolina en el recorrido es {Consumo_gasolina:.2f} litros")
print(f"El costo en gasolina del recorrido es: {Costo_gasolina:.2f} Bs.")
print(f"La velocidad media durante el recorrido, en Km/h es: {Velocidad_media_Kmh:.2f} Kms")
print(f"La velocidad media durante el recorrido, en m/s  {Velocidad_media_ms:.2f} mts/seg")



