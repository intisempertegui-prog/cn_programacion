#Descuento e IVA en un producto
#Datos Iniciales
name_product = "Televisor Samsung 55 Pulgadas"
price_product = 545
IVA = 0.12
discount = 0.10
total=0

price_product += price_product * IVA
print("Precio del producto con iva", price_product)
   
price_product -= price_product * discount
print (f"El precio del producto {name_product} con descuento es: {price_product}")

total = price_product

print(f"El precio del producto {name_product} es de: {total} ")