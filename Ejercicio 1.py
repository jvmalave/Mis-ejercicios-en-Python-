# Diseñar un programa en Python que lea el valor de una distancia 
# en millas marinas y la escriba expresada en metros. 
# Sabiendo que 1 milla marina equivale a 1852 metros.


print("-------------------------------------------------------")
print("Programa que convierte las millas marinas a metros")
print("-------------------------------------------------------")


Distancia_mts=0
Distancia_milla=0
Factor_conversión=1852
intentos=1
Distancia_milla=float(input("Por favor ingrese el valor de la distancia en mIllas marinas "))
while(Distancia_milla<0):
        Distancia_milla=float(input("La distancia en milla no puede ser negativo, por favor introduzca un valor positvo "))
        if intentos==2:
                print("Has realizados muchos intentos")
                print("El programa ha finalizado")
                break;
        if Distancia_milla<0:
                intentos=intentos+1
if intentos<3:
        Distancia_mts=Distancia_milla*Factor_conversión
        print(f"La distancia en metros es: {Distancia_mts} metros")

