
print("----SISTEMA DE CONTROL Y GESTION DE UNA FARMACIA----")
print("----------------------------------------------------")
usuarios={} ##Usaremos este array para guardar los usuarios
inventario=[] ##Usaremos esta lista para el los productos
ventas=[] ##Usaremos esta lista para registrar las ventas
##Funciones para la pantalla de Login-------------------
##Funcion de registrar
def registrar():
    print("--------Registro--------")
    usuario=input("Ingrese un nuevo usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe")
        return
    password=input("Ingrese contraseña: ")
    usuarios[usuario]=password
    print("Usuario registrado correctamente!")
##Funcion de login
def login():
    print("--------Iniciar Sesion--------")
    usuario=input("Usuario: ")
    password=input("Contraseña: ")
    if usuario in usuarios and usuarios[usuario]==password:
        print(f"\n Bienvenido {usuario}")
        menu_principal(usuario)
    else:
        print("Usuario o contraseña incorrecta, revise!")

##Funcion Agregar producots
def agregar_producto():
    print("-------Agregar Producto--------")
    nombre=input("Ingrese nombre del producto: ")
    precio=float(input("Ingrese precio del producto: "))
    stock=int(input("Ingrese stock del producto: "))
    producto={
        "nombre":nombre,
        "precio":precio,
        "stock":stock
    }
    inventario.append(producto) ## .append es para agregar un elemento al final de la lista
    print("Producto guardado exitosamente!")

##Funcion Ver Inventario de productos
def ver_inventario():
    print("===Inventario de Productos===")
    if len(inventario)==0:
        print("No hay productos registrados")
        return
    for i, producto in enumerate(inventario):
         print(f"Id: {i+1} - Nombre: {producto['nombre']} - Precio Bs: {producto['precio']} - Stock: {producto['stock']}") ##Variables de prdocuto
         print("==============================================")

##Funcion Modificar productos
def modificar_producto():
    print("===Modificar Productos===")
    ver_inventario()
    if len(inventario)==0:
        return
    indice=int(input("Ingrese ID del producto a modificar: "))-1##con este (-1) cambio la posicion a una anterior y tomo en cuenta la posicion 0
    if indice>=0 and indice<len(inventario):
        print("Ingrese los nuevos datos: ")
        new_nombre=input("Nuevo nombre del producto: ")
        new_precio=float(input("Nuevo precio del producto: "))
        new_stock=int(input("Nuevo stock del producto: "))
        inventario[indice]["nombre"]= new_nombre
        inventario[indice]["precio"]=new_precio
        inventario[indice]["stock"]=new_stock
        print("Producto modificado correctamente!")
    else:
        print("Producto no valido")

##Funcion Eliminar Producto
def eliminar_producto():
    print("===Eliminar Productos===")
    ver_inventario()
    if len(inventario)==0:
        return
    indice=int(input("Ingrese ID del producto a Eliminar"))-1 ##con este (-1) cambio la posicion a una anterior y tomo en cuenta la posicion 0
    if indice>=0 and indice<len(inventario):
        producto_eliminado=inventario.pop(indice) ## .pop para eliminar de la lista(aca se pone la posicion)
        print(f"Producto Eliminado: {producto_eliminado}")
    else:
        print("Producto no Valido")

##Funcion Registrar Ventas
def registrar_venta():
    print("======Registrar Venta======")
    print("===========================")
    ver_inventario()
    if len(inventario)==0:
        return
    indice=int(input("Ingrese la ID del producto"))
    if indice>=0 and indice<len(inventario):
        producto=inventario[indice]
        cantidad=int(input("Cantidad a vender: "))
        if cantidad<=0:
            print("Cantidad Invalida")
        elif cantidad>producto["stock"]:
            print("Stock insuficiente")
            return
        total=cantidad*producto["precio"]

        producto["stock"]-=cantidad ##Descontar Stock

        venta={"producto":producto["nombre"], "cantidad":cantidad, "total":total}

        ventas.append(venta) ##con append cuardamos la "Venta" en la lista de Ventas que añadimos al inicio

        print("Venta realizada Exitosamente")
        print(f"Producto: {producto['nombre']} - Cantidad: {cantidad} - Total: Bs. {total}")
    else:
        print("ID no valido")

##Funcion para ver las ventas
def ver_ventas():
    print("======Historial Ventas======")
    print("============================")

    if len(ventas)==0:
        print("No hay ventas registradas")
        return
    total_general=0

    for i, venta in enumerate(ventas):
        print(f"Venta{i} - Producto: {venta['producto']} - Cantidad: {venta['cantidad']} - Total: {venta['total']}")
        total_general+=venta["total"]

    print(f"Total Vendido: Bs. {total_general}")



##Menus---------------------------------

##Menu Ventas
def menu_ventas():
    while True:
        print("-----SISTEMA  FARMACIA-----")
        print("------Menu Ventas-----")
        print("1.Registrar Ventas")
        print("2.Ver ventas")
        print("3.Atras")
        opV=input("Seleccione una opcion")
        if opV=="1":
            registrar_venta()
        elif opV=="2":
            ver_ventas()
        elif opV=="3":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")

##Menu de Inventario
def menu_inventario():
    while True:
        print("-----SISTEMA  FARMACIA-----")
        print("------Menu Inventario-----")
        print("1.Agregar Producto")
        print("2.Modificar Producto")
        print("3.Eliminar Producto")
        print("4.Ver Inventario")
        print("5.Atras")
        opI=input("Seleccione una opcion: ")
        if opI=="1":
            agregar_producto()
        elif opI=="2":
            modificar_producto()
        elif opI=="3":
            eliminar_producto()
        elif opI=="4":
            ver_inventario()
        elif opI=="5":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida")

##Funcion Menu principal
def menu_principal(usuario):
    while True:
        print("\n---------Sistema FARMACIA-----------")
        print("============Menu Principal============")
        print("1.Inventario")
        print("2.Ventas")
        print("3.Cerrar")
        opMP=input("Seleccione una opcion: ")
        if opMP=="1":
            menu_inventario()
        elif opMP=="2":
            menu_ventas()
        elif opMP=="3":
            print("Cerrando Sesion...")
            break
        else:
            print("Opcion invalida")






##Menu Login

while True:
    print("-------------LOGIN-----------")
    print("=============================")
    print("Seleccione opcion con numero:")
    print("1.Iniciar Sesion")
    print("2.Registrarse")
    print("3.Salir")
    op=input("Ingrese opcion deseada(1,2,3):")
    if op=="2":
        registrar()
    elif op=="1":
        login()
    elif op=="3":
        print("Saliendoo...")
        break
    else:
        print("Opcion invalida, intente nuevamente")
