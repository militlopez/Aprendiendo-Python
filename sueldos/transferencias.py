import tkinter as tk
ARCHIVO="empleados.txt"

def main(): 
    print(f"Acreditación de Sueldos")

def calcular():
    # ARCHIVO (mayus) es una constante y archivo (minus) es una variable
    with open(ARCHIVO,"r",encoding="utf-8") as archivo:
        total = 0.0
        cantidad = 0 
        for linea in archivo:
# strip "limpia" las lineas para que no tenga espacios
            empleado=linea.strip()
# se puede tomar cualquiera de las 2 variables (empleado o linea)
# != distinto "" vacio
            if empleado!="": 
                legajo,nombre,cbu,salario=empleado.split(";")
                salario=float(salario)
                print(f"Se transfirió al cbu {cbu} el monto de ${salario}")
                total=total+salario
                cantidad=cantidad+1
        lbl_cantidad.config(text=f"Empleados: {cantidad}")
        lbl_total.config(text=f"Total a depositar: ${total:.2f}")

if __name__ == "__main__":
    try:
        main()
        # --- Construcción de la ventana ---
        ventana=tk.Tk()
        ventana.title("Transferencias")
        ventana.geometry("350x200")
        lbltitulo=tk.Label(ventana,text="Resumen de Transferencias",font=("Arial",15,"bold"))
        lbltitulo.pack(pady=10)
        btn_calcular=tk.Button(ventana,text="Transferir",command=calcular)
        btn_calcular.pack(pady=10)
        lbl_cantidad = tk.Label(ventana, text="Empleados: -", font=("Arial", 12))
        lbl_cantidad.pack(pady=5)
        lbl_total = tk.Label(ventana, text="Total a depositar: -", font=("Arial", 12))
        lbl_total.pack(pady=5)
        ventana.mainloop()
    except FileNotFoundError:
        print("No se encontró el archivo.")
