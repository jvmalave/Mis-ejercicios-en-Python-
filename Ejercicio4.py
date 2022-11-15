#Diseñar un programa que calcule el área y el perímetro de un triángulo rectángulo dada la base y la altura.


print("----------------------------------------------------------------------")
print("Programa que calcula el área y perimetro de un trriangulo rectangulo")
print("----------------------------------------------------------------------")


import math

Base_triangulo=0
Altura_triangulo=0

Tipo_triangulo=input("El tipo de triangulo es rectangulo si:s o no:n ")


if(Tipo_triangulo=="s"):
    Base_triangulo=float(input("Por favor ingrese la base de triangulo en cm: "))
    while Base_triangulo<0:
        Base_triangulo=float(input("La base del triangulo no puede ser negativa, Por favor ingrese un valor positivo de la base de triangulo en cm: "))

    Altura_triangulo=float(input("Por favor ingrese la altura de triangulo en cm: ")) 
    while Altura_triangulo<0:
        Altura_triangulo=float(input("La altura del triangulo no puede ser negativa, Por favor ingrese un valor positivo de la altura de triangulo en cm: "))
    
    Area_triangulo=(Base_triangulo*Altura_triangulo)/2
    Hipotenusa_Triangulo=math.sqrt((Base_triangulo**2)+(Altura_triangulo**2))
    Perimetro_triangulo=Base_triangulo+Altura_triangulo+Hipotenusa_Triangulo
    
    print(f"El área del triangulo es: {Area_triangulo:.2f} cm^2")
    print(f"La hipotenusa de triangulo es: {Hipotenusa_Triangulo:.2f} cm")
    print(f"El perimetro del triangulo es: {Perimetro_triangulo:.2f} cm")

else:
    Base_triangulo=float(input("Por favor ingrese la base de triangulo en cm ")) 
    while Base_triangulo<0:
        Base_triangulo=float(input("La base del triangulo no puede ser negativa, Por favor ingrese un valor positivo de la base de triangulo en cm "))
    
    Altura_triangulo=float(input("Por favor ingrese la altura de triangulo en cm ")) 
    while Altura_triangulo<0:
        Altura_triangulo=float(input("La altura del triangulo no puede ser negativa, Por favor ingrese un valor positivo de la altura de triangulo en cm"))
    
    Area_triangulo=(Base_triangulo*Altura_triangulo)/2
    
    print(f"El área del triangulo es: {Area_triangulo:.2f} cm^2")
    print("Al no ser un triangulo rectangulo, el perimetro no se puede calcular con los datos disponibles")