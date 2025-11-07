# PROGRAMA: DESCUENTO POR COMPRA DE ESCRITORIOS

cantidad = int(input("Ingrese la cantidad de escritorios que quiere comprar: "))

valor_escritorio = 10000

if cantidad < 5:
    descuento = 0.10
elif cantidad < 10:
    descuento = 0.20
else:
    descuento = 0.40

total_compra = valor_escritorio * cantidad
total_descuento = total_compra * descuento
total_pagar = total_compra - total_descuento

print("Cantidad de escritorios:", cantidad)
print("Precio unitario: $", valor_escritorio)
print("Descuento aplicado:", descuento * 100, "%")
print("Total a pagar: $", total_pagar)