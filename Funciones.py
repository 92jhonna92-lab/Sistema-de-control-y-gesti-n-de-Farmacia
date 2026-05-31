usuarios={} ##Usaremos este array para guardar los usuarios
inventario=[] ##Usaremos esta lista para el los productos
ventas=[] ##Usaremos esta lista para registrar las ventas

import Inicio
##Funciones para la pantalla de Login-------------------
##Funcion de registrar
def registrar():
    print("--------Registro--------")
    usuario=input("Ingrese un nuevo usuario: ")
    if len(usuario)>=8:
        print("Usuario guardado")
    else:
        print("Usuario invalido minimo 8 caracteres")
        return 
    if usuario in usuarios:
        print("El usuario ya existe")
        return
    password=input("Ingrese contraseña: ")
    if len(password)>=8:
        print("Contraseña guardada")
    else:
        print("Contraseña insegura")
    usuarios[usuario]=password
    print("Usuario registrado correctamente!")
##Funcion de login
def login():
    print("--------Iniciar Sesion--------")
    usuario=input("Usuario: ")
    password=input("Contraseña: ")
    if usuario in usuarios and usuarios[usuario]==password:
        print(f"\n Bienvenido {usuario}")
        Inicio.menu_principal(usuario)
    else:
        print("Usuario o contraseña incorrecta, revise!")

        ##Funcion Agregar producots
def agregar_producto():
    print("-------Agregar Producto--------")
    nom=input("Ingrese nombre del producto: ")
    nombre=nom.upper()
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
        new_nom=input("Nuevo nombre del producto: ")
        new_nombre=new_nom.upper()
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
    indice=int(input("Ingrese ID del producto a Eliminar: "))-1 ##con este (-1) cambio la posicion a una anterior y tomo en cuenta la posicion 0
    if indice>=0 and indice<len(inventario):
        producto_eliminado=inventario.pop(indice) ## .pop para eliminar de la lista(aca se pone la posicion)
        print(f"Producto Eliminado: {producto_eliminado}")
    else:
        print("Producto no Valido")


##Funcion Registrar Ventas
def registrar_venta():
    print("======Registrar Venta======")
    print("===========================")
    
    if len(inventario)==0:
        print("No hay productos en el inventario") 
        return
    total_general=0

    while True: ##Vamos a usar un while para que entre en un bucle de ventas hasta que el ID este en blanco/presione enter
        ver_inventario()
        entrada=input("Ingrese la ID del producto: (Enter para finalizar) ") ##Si presiona enter se finaliza la venta
        if entrada== "":
            break
        indice=int(entrada)-1

        if indice>=0 and indice<len(inventario):

            producto=inventario[indice]
            cantidad=int(input("Cantidad a vender: "))
            if cantidad<=0:
                print("Cantidad Invalida")
                continue
            elif cantidad>producto["stock"]:
                print("Stock insuficiente")
                continue
            total=cantidad*producto["precio"]
            producto["stock"]-=cantidad ##Descontar Stock
            venta={"producto":producto["nombre"], "cantidad":cantidad, "total":total}
            ventas.append(venta) ##con append cuardamos la "Venta" en la lista de Ventas que añadimos al inicio
            total_general+=total
            print("Venta realizada Exitosamente")
            print(f"Producto: {producto['nombre']} - Cantidad: {cantidad} - Total: Bs. {total}")
        else:
            print("ID no valido")
    print("======Resumen de Venta=======")
    print(f"Total Vendido: Bs. {total_general}")

##Funcion para ver las ventas
def ver_ventas():
    print("======Historial Ventas======")
    print("============================")

    if len(ventas)==0:
        print("No hay ventas registradas")
        return
    total_general=0

    for i, venta in enumerate(ventas):
        print(f"Venta{i+1} - Producto: {venta['producto']} - Cantidad: {venta['cantidad']} - Total: {venta['total']}")
        total_general+=venta["total"]

    print(f"Total Vendido: Bs. {total_general}")