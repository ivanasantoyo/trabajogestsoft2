#La lista de almacen estara conformada por frutas, verduras y productos de limpieza.

#FRUTAS

Frutas = []
x = 0
while x != "NO":
    f=input("¿Que fruta desea comprar? ")
    Frutas.append (f)
    x = input ("¿Desea agregar otra fruta? para continuar escriba SI de lo contrario escriba NO: ") 

print("Las frutas seleccionadas son: ")
print(Frutas)

#VERDURAS

Verduras = []
x = 0
while x != "NO":
    v=input("¿Que verdura desea comprar? ")
    Verduras.append (v)
    x = input ("¿Desea agregar otra verdura? para continuar escriba SI de lo contrario escriba NO: ") 

print("Las verduras seleccionadas son: ")
print(Verduras)


#PRODUCTOS DE LIMPIEZA
