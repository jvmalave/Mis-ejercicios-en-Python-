# Diseñar un programa que escribe el porcentaje descontado
# en una compra, introduciendo por teclado el porcentaje descontado y el precio pagado.


print("--------------------------------------------------------------")
print("Programa que escribe el porcentade de descuento en una compra ")
print("--------------------------------------------------------------")


Precio_pagado=0
Porcentaje_descuento=0

Porcentaje_descuento=float(input("Por favor ingrese el porcetaje de descuento "))
while(Porcentaje_descuento<0 or Porcentaje_descuento >100):
    Porcentaje_descuento=float(input("El porcentaje de descuento no puede ser negativo ni superior a 100%, por favor ingrese un valor positivo entre 0 y 100 "))

Precio_pagado=float(input("Por favor ingrese el precio pagado "))
while(Precio_pagado<0):
    Precio_pagado=float(input("El precio pagado no puede ser negativo, por favor ingrese un valor positivo "))

Precio_venta=Precio_pagado/(1-(Porcentaje_descuento/100))
Monto_descontado=Precio_venta*(Porcentaje_descuento/100)

print(f"El precio de venta del producto es: Bs. {Precio_venta:.2f}")
print(f"El Porcentaje_descuento aplicado es: {Porcentaje_descuento:.2f} %")
print(f"El monto descontado es: Bs. {Monto_descontado:.2f}")
print(f"El precio pagado despues de aplicar descuento es: Bs. {Precio_pagado:.2f}")


