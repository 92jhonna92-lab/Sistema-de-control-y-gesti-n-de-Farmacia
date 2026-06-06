usuarios={} ##Usaremos este array para guardar los usuarios
inventario=[] ##Usaremos esta lista para el los productos
ventas=[] ##Usaremos esta lista para registrar las ventas
facturas=[]

##import Inicio
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
        
        return usuario ##devolvemos usuario
    
        ##Inicio.menu_principal(usuario) ##aCA Estaba mezclando
    else:
        print("Usuario o contraseña incorrecta, revise!")
        return False ##devuelvo false

        ##Funcion Agregar producots
def agregar_producto():
    print("-------Agregar Producto--------")
    nom=input("Ingrese nombre del producto: ")
    nombre=nom.upper()
    while True: ##Validamos el precio de float
        try:
            precio=float(input("Ingrese precio del producto: "))
            if precio<=0:
                print("El precio debe ser mayor a 0")
                continue

            break

        except ValueError:
            print("No se permiten letras en el precio")

    while True:
        try:
            stock=int(input("Ingrese stock del producto: "))
            if stock<0:
                print("El stock no debe ser negativo")
                continue
            break
        except ValueError:
            print("No se permiten letras en el stock")

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
    try:
        indice=int(input("Ingrese ID del producto a modificar: "))-1##con este (-1) cambio la posicion a una anterior y tomo en cuenta la posicion 0
        
        if indice<0 or indice>=len(inventario):
            print("ID no Valido ")
            return
    except ValueError:
        print("El ID debe ser un numero")
        return
    new_nom=input("Nuevo nombre del producto: ")
    new_nombre=new_nom.upper()
    while True: ##Validamos que no se pueda escribir letras en los precios-----
        try:
            new_precio=float(input("Nuevo precio del producto: "))
            if new_precio<=0:
                print("El precio debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("No se permiten letras en el precio")
    while True:
        try:
            new_stock=int(input("Nuevo stock del producto: "))
            if new_stock<0:
                print("El stock no puede ser negativo")
                continue
            break
        except ValueError:
            print("No se permiten letras en el stock")

    inventario[indice]["nombre"]= new_nombre
    inventario[indice]["precio"]=new_precio
    inventario[indice]["stock"]=new_stock
    print("Producto modificado correctamente!")

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
    ##Datos del cliente
    while True:
        nombre_cliente=input("Nombre o Razon Social: ").strip()
        caracteres_permitidos=" .,-&()"
        if nombre_cliente == "":
            print("El nombre no puede estar vacio")
            continue

        elif not all(
            c.isalpha() or c.isspace() for c in caracteres_permitidos 
            for c in nombre_cliente):
            ##.isalpha verifica que todos los caracteres sean letras del alfabeto
            ##.isspace verifica si todos los caracteres en una cadena son espacios en blanco
            print("Solo se permiten letras y caracteres especiales")
            continue
        break
    while True:
        nit_cliente=input("NIT/CI:").strip()
        if nit_cliente=="":
            print("El NIT/CI no puede estar vacio")
            continue
        elif not nit_cliente.isdigit(): ##.esidigit verifica que sea un numero
            print("El NIT/CI solo puede contener numeros")
            continue
        break

    ##Variable y lista para registrar la facura y el total
    lista_factura=[]
    total_general=0

    if len(inventario)==0:
        print("No hay productos en el inventario") 
        return
    

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

            lista_factura.append({
                "producto":producto["nombre"], "cantidad":cantidad, "precio":producto["precio"], "subtotal":total##Estos datos los guardamos en lista
            })
            total_general+=total
            print("Venta realizada Exitosamente")
            print(f"Producto: {producto['nombre']} - Cantidad: {cantidad} - Total: Bs. {total}")
        else:
            print("ID no valido")

    ##Dibujamos La Factura

    print("\n===================================")
    print("          FARMACIA    ")
    print("===================================")
    print(f"Cliente: {nombre_cliente}")
    print(f"NIT/CI : {nit_cliente}")
    print("===================================")
    print("Producto      Cant   Subtotal")

    for item in lista_factura:
        print(
            f"{item['producto']:<12} "
            f"{item['cantidad']:<5} "
            f"Bs.{item['subtotal']}"
            )
    print("===================================")
    print(f"TOTAL: Bs.{total_general}")
    print("===================================")
    ##Vamos a guardar esta factura en una array(usamos array porque tenemos definido lo que usaremos)
    factura={"cliente": nombre_cliente, "nit":nit_cliente, "items":lista_factura,"total":total_general}
    facturas.append(factura) ##aca guardamos con el .append el array de arriba en la lista de facturas


def ver_facturas():
    print("===Historial Facturas===")
    if len(facturas)==0:
        print("No hay facturas registradas")
        return
    for i, factura in enumerate(facturas):

        print(f"\nFactura #{i+1}")
        print(f"Cliente: {factura['cliente']}")
        print(f"NIT/CI: {factura['nit']}")
        print("---------------------------------")
        print("\nProductos:")

        for item in factura["items"]:
            print(
                f"- {item['producto']} "
                f"x {item['cantidad']} "
                f"= Bs.{item['subtotal']}"
            )
        print(f"\nTOTAL: Bs.{factura['total']}")
        print("======================================")

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