import pandas as pd
import matplotlib.pyplot as plt

primer_mes=input("Primer mes de comparación (archivo): ")
segundo_mes=input("Segundo mes de comparación (archivo): ")
# print(primer_mes)
# print(segundo_mes)
ventas_mes_1=pd.read_excel(primer_mes,sheet_name="Ventas")
ventas_mes_2=pd.read_excel(segundo_mes,sheet_name="Ventas")
# print(ventas_mes_1)
# print(ventas_mes_2)
# len cuenta la c/de filas
print(f"Filas {primer_mes}: {len(ventas_mes_1)} | Filas {segundo_mes}: {len(ventas_mes_2)}")

ventas=pd.concat([ventas_mes_1,ventas_mes_2],ignore_index=True)
# print(ventas)
# print(len(ventas))
print(f"Cantidad de Filas de la unión: {len(ventas)}")

ventas["Facturación"]=ventas["Precio_Unitario"]*ventas["Unidades"]
negocios=pd.read_excel(primer_mes,sheet_name="Negocios")
ventas=ventas.merge(negocios,on="Negocio",how="left")
#print(ventas)
totales=ventas.groupby("Mes",sort=False)[["Unidades","Facturación"]].sum()
print(totales)
# === Gráfico ===
fig, ejes = plt.subplots(1, 2, figsize=(13, 6))
fig.suptitle("Comparación de ventas de alfajores", fontsize=16, fontweight="bold")

totales["Unidades"].plot(kind="bar",ax=ejes[0],rot=0,title="Unidades Vendidas",color=["red","orange"])
totales["Facturación"].plot(kind="bar",ax=ejes[1],rot=0,title="Total Facturado",color=["blue","skyblue"])

ejes[0].bar_label(ejes[0].containers[0])
ejes[1].bar_label(ejes[1].containers[0])

plt.show()