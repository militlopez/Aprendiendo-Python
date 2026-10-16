import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

ARCHIVO = "ventas.txt"
COLUMNAS = ("Tipo de madera", "Valor", "Fecha", "Cliente", "Entrega")


# ---------- Lógica de archivo ----------

def guardar_venta(tipo, precio, fecha, cliente, entrega):
    """Agrega una venta al final del archivo (mismo formato que antes)."""
    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(f"{tipo} \t {precio} \t {fecha} \t {cliente} \t {entrega} \n")


def leer_ventas():
    """Devuelve la lista de ventas guardadas. Si el archivo no existe, lista vacía."""
    ventas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                campos = [c.strip() for c in linea.split("\t")]
                if len(campos) == len(COLUMNAS):
                    ventas.append(campos)
    except FileNotFoundError:
        pass
    return ventas


# ---------- Interfaz gráfica ----------

class AppVentas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de ventas de madera")
        self.minsize(640, 460)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._crear_formulario()
        self._crear_tabla()
        self._cargar_tabla()

    def _crear_formulario(self):
        marco = ttk.LabelFrame(self, text="Nueva venta", padding=10)
        marco.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        marco.columnconfigure(1, weight=1)

        self.var_tipo = tk.StringVar()
        self.var_precio = tk.StringVar()
        self.var_fecha = tk.StringVar(value=date.today().strftime("%d/%m/%Y"))
        self.var_cliente = tk.StringVar()
        self.var_entrega = tk.StringVar()

        campos = [
            ("Tipo de madera:", self.var_tipo),
            ("Valor de la venta:", self.var_precio),
            ("Fecha de la venta:", self.var_fecha),
            ("Cliente:", self.var_cliente),
            ("Condición de entrega:", self.var_entrega),
        ]

        self.entradas = []
        for fila, (texto, variable) in enumerate(campos):
            ttk.Label(marco, text=texto).grid(row=fila, column=0, sticky="w", pady=3)
            entrada = ttk.Entry(marco, textvariable=variable)
            entrada.grid(row=fila, column=1, sticky="ew", padx=(10, 0), pady=3)
            entrada.bind("<Return>", lambda e: self.registrar())
            self.entradas.append(entrada)

        botones = ttk.Frame(marco)
        botones.grid(row=len(campos), column=0, columnspan=2, sticky="e", pady=(10, 0))
        ttk.Button(botones, text="Limpiar", command=self.limpiar).pack(side="left", padx=5)
        ttk.Button(botones, text="Registrar venta", command=self.registrar).pack(side="left")

        self.entradas[0].focus()

    def _crear_tabla(self):
        marco = ttk.LabelFrame(self, text="Ventas registradas", padding=10)
        marco.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        marco.columnconfigure(0, weight=1)
        marco.rowconfigure(0, weight=1)

        self.tabla = ttk.Treeview(marco, columns=COLUMNAS, show="headings")
        for col in COLUMNAS:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=110, anchor="w")

        scroll = ttk.Scrollbar(marco, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)

        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll.grid(row=0, column=1, sticky="ns")

    def _cargar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        for venta in leer_ventas():
            self.tabla.insert("", "end", values=venta)

    def limpiar(self):
        self.var_tipo.set("")
        self.var_precio.set("")
        self.var_fecha.set(date.today().strftime("%d/%m/%Y"))
        self.var_cliente.set("")
        self.var_entrega.set("")
        self.entradas[0].focus()

    def registrar(self):
        tipo = self.var_tipo.get().strip()
        precio = self.var_precio.get().strip()
        fecha = self.var_fecha.get().strip()
        cliente = self.var_cliente.get().strip()
        entrega = self.var_entrega.get().strip()

        # Validaciones
        if not all([tipo, precio, fecha, cliente, entrega]):
            messagebox.showwarning("Faltan datos", "Completá todos los campos.")
            return
        try:
            float(precio.replace(",", "."))
        except ValueError:
            messagebox.showwarning("Valor inválido", "El valor de la venta debe ser un número.")
            return

        # Guardado con el mismo manejo de errores del script original
        try:
            guardar_venta(tipo, precio, fecha, cliente, entrega)
        except PermissionError:
            messagebox.showerror("Error", "Error en los permisos.")
            return
        except OSError as error:
            messagebox.showerror("Error", f"Problemas con el archivo usando el SO {error}.")
            return

        self.tabla.insert("", "end", values=(tipo, precio, fecha, cliente, entrega))
        messagebox.showinfo("Listo", "Venta registrada correctamente.")
        self.limpiar()


def main():
    app = AppVentas()
    app.mainloop()


if __name__ == "__main__":
    main()
