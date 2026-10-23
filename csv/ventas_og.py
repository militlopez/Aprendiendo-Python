import csv
import matplotlib.pyplot as plt

totales={}
unidades={}

with open("ventas.csv",encoding="utf-8",newline="") as archivo:
    lector=csv.DictReader(archivo,delimiter=";")
    for fila in lector:
        cantidad=int(fila["cantidad"])
        sucursal=fila["sucursal"]
        producto=fila["producto"]
        precio=float(fila["precio_unitario"].replace(",","."))
        #print(f"{cantidad} {sucursal} {producto} {precio}")
        totales[sucursal]=totales.get(sucursal,0)+cantidad*precio
        unidades[producto]=unidades.get(producto,0)+cantidad 
    print(totales)
    print(unidades)
valores=list(totales.values())
print(valores)
sucursales=list(totales.keys())
print(sucursales)
# Gráfico de barras
barras=plt.bar(sucursales,valores,color="purple")
plt.bar_label(barras,fmt="%.2f")
plt.xlabel("Sucursales")
plt.ylabel("Total Neto ($)")
plt.title("Total Neto por Sucursal")
plt.show()