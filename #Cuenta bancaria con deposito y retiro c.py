#Cuenta bancaria con deposito y retiro con intereses y comisiones
cuenta_bancaria = 0
deposito = 500
retiro = 0

if deposito >= 200:
    cuenta_bancaria += deposito
    cuenta_bancaria += cuenta_bancaria * 0.03
    print("Deposito realizado es:", cuenta_bancaria)

deposito = 100

if deposito >= 200:
    cuenta_bancaria += deposito
    cuenta_bancaria += cuenta_bancaria * 0.03
    print("Deposito realizado es:", cuenta_bancaria)

cuenta_bancaria += deposito
print("total de cuenta:", cuenta_bancaria)

retiro = 300

if retiro >=300:
    cuenta_bancaria -= retiro
    cuenta_bancaria -= cuenta_bancaria * 0.01
    print("Una vez realizado el retiro usted tiene:", cuenta_bancaria)

print("El total es:", cuenta_bancaria)