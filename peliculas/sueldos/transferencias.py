def main(): 
    ARCHIVO="empleados.txt"
    print("-"*80)
    total = 0.0
    cantidad = 0
    print(f"Acreditación de Sueldos")
    print("-"*80)
# ARCHIVO (mayus) es una constante y archivo (minus) es una variable
    with open(ARCHIVO,"r",encoding="utf-8") as archivo:
        for linea in archivo:
# strip "limpia" las lineas para que no tenga espacios
            empleado=linea.strip()
# separa la info con ; y le da nombre a c/u
            legajo,nombre,cbu,salario=empleado.split(";")
            # print(cbu)
            salario=float(salario)
            print(f"Se transfirió al cbu {cbu} el monto de ${salario}")
            total=total+salario
            cantidad=cantidad+1
        print(f"El monto total a transferir es ${total}.")
        print(f"La cantidad de montos transferidos es {cantidad}.")

if __name__ == "__main__":
	main()
