import csv
import matplotlib.pyplot as plt 
from collections import Counter

categorias_reclamos=[]

with open("reclamos.csv","r",encoding="utf-8") as archivo:
    lector=csv.DictReader(archivo)
    for fila in lector:
        categorias_reclamos.append(fila["categoria"])
# toma la lista y cuenta cuantas hay 
conteo=Counter (categorias_reclamos)
# Gráfico
barras=plt.bar(conteo.keys(),conteo.values(),color="purple",edgecolor="red")
plt.bar_label(barras,fontsize=11,weight="bold",padding=3)
plt.title("Cantidad de reclamos por categoría",fontsize=14,weight="bold",fontfamily="tahoma")
plt.xlabel("Categoría")
plt.ylabel("Cantidad")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.show()