ARCHIVO="ventas.txt"

def cargar_ventas():
    try:
        with open(ARCHIVO,"a",encoding="utf-8") as archivo:
            tipo=input("Tipo de madera: ")
            precio=input("Valor de la venta: ")
            fecha=input("Fecha de la venta: ")
            cliente=input("Cliente: ")
            entrega=input("Condición de entrega: ")
            archivo.write(f"{tipo} \t {precio} \t {fecha} \t {cliente} \t {entrega} \n")
    except PermissionError:
        print("Error en los permisos.")
    except OSError as error:
        print(f"Problemas con el archivo usando el SO {error}.")

def main():
    seguir="s"
    while(seguir=="s"):
        cargar_ventas()
        seguir=input("¿Necesita registrar otra venta?").lower()

if __name__ =="__main__":
    main()