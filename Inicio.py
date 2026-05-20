
print("----SISTEMA DE CONTROL Y GESTION DE UNA FARMACIA----")
print("----------------------------------------------------")
##Funcion de registrar
def registrar():
    print("--------Registro--------")
    usuario=input("Ingrese un nuevo usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe")
        return
    password=input("Ingrese contraseña: ")
    usuario[usuarios]=password
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
##Funcion Menu principal
def menu_principal(usuario):
    while True:
        print("\n---------Sistema FARMACIA--------")
        print("1. Inventario")
        print("2.Ventas")
        print("Cerrar")

##Menu Login
usuarios={}
while True:
    print("-------------LOGIN-----------")
    print("Seleccione opcion con numero:")
    print("1.Iniciar Sesion")
    print("2.Registrarse")
    print("3.Cerrar Sesion")
    op=input("Ingrese opcion deseada(1 o 2):")
    if op=="1":
        registrar()
    elif op=="2":
        login()
    elif op=="3":
        print("Adios")
        break
    else:
        print("Opcion invalida, intente nuevamente")
