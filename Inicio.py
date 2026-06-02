
import Funciones 
## Importamos la carpeta funciones del mismo proyecto para llamarlos.
print("----SISTEMA DE CONTROL Y GESTION DE UNA FARMACIA----")
print("----------------------------------------------------")


##Menus---------------------------------

##Menu Ventas
def menu_ventas():
    while True:
        print("-----SISTEMA  FARMACIA-----")
        print("------Menu Ventas-----")
        print("1.Registrar Ventas")
        print("2.Ver ventas")
        print("3.Atras")
        opV=input("Seleccione una opcion: ")
        if opV=="1":
            Funciones.registrar_venta()
        elif opV=="2":
            Funciones.ver_ventas()
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
            Funciones.agregar_producto()
        elif opI=="2":
            Funciones.modificar_producto()
        elif opI=="3":
            Funciones.eliminar_producto()
        elif opI=="4":
            Funciones.ver_inventario()
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
        Funciones.registrar()
    elif op=="1":
        usuario=Funciones.login() ##
        if usuario!=False:
            menu_principal(usuario)
    elif op=="3":
        print("Saliendoo...")
        break
    else:
        print("Opcion invalida, intente nuevamente")
