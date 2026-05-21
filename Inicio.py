
print("----SISTEMA DE CONTROL Y GESTION DE UNA FARMACIA----")
print("----------------------------------------------------")
usuarios={}
inventario=[]
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
    print("Agregar Producto")
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
    ver_inventario()
    if len(inventario)==0:
        return
    indice=int(input("Ingrese ID del producto a modificar: "))
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
    ver_inventario()
    if len(inventario)==0:
        return
    indice=int(input("Ingrese ID del producto a Eliminar"))
    if indice>=0 and indice<len(inventario):
        producto_eliminado=inventario.pop(indice) ## .pop para eliminar de la lista(aca se pone la posicion)
        print(f"Producto Eliminado: {producto_eliminado}")
    else:
        print("Producto no Valido")


##Menus---------------------------------

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
        print("\n---------Sistema FARMACIA--------")
        print("1. Inventario")
        print("2.Ventas")
        print("3.Cerrar")
        opMP=input("Seleccione una opcion: ")
        if opMP=="1":
            menu_inventario()
        elif opMP=="2":
            print("Aqui se registraran las ventas")
        elif opMP=="3":
            print("Cerrando Sesion...")
            break
        else:
            print("Opcion invalida")






##Menu Login

while True:
    print("-------------LOGIN-----------")
    print("Seleccione opcion con numero:")
    print("1.Iniciar Sesion")
    print("2.Registrarse")
    print("3.Cerrar Sesion")
    op=input("Ingrese opcion deseada(1,2,3):")
    if op=="2":
        registrar()
    elif op=="1":
        login()
    elif op=="3":
        print("Cesion cerrada.!")
        break
    else:
        print("Opcion invalida, intente nuevamente")
