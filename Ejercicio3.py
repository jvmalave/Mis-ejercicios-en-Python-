# Diseñar un programa que pida por teclado dos números enteros 
# y muestre su suma y multiplicación.


print("-----------------------------------------------------")
print("Programa que suma y multiplica dos números enteros")
print("------------------------------------------------------")



def valida_entero(entrada):
 
   while True:
       try:
           entrada=int(entrada)
           return(entrada)
       except ValueError:
           entrada=input("La entrada NO es un entero, Por favor ingrese un numero entero ")
           

Numero1=0
Numero2=0

Numero1=input("Por favor ingrese el valor del primer número ")      
Numero1=valida_entero(Numero1)
Numero2=input("Por favor ingrese el valor del segundo número ")
Numero2=valida_entero(Numero2)

suma=Numero1+Numero2
multiplica=Numero1*Numero2
print(f"La suma de los dos números es: {suma} ")
print(f"La multilplicación de los dos números es: {multiplica} ")
