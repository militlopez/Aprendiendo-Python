#pip install pandas
#pip install openpyxl
import pandas as pd 
import matplotlib.pyplot as plt
# dataframe de pandas
nombre_planilla=input("Ingrese el nombre de la planilla")

ventas=pd.read_excel(nombre_planilla,sheet_name="Ventas")
negocios=pd.read_excel(nombre_planilla,sheet_name="Negocios")

#print(ventas.describe())
#print(ventas["Precio_Unitario"])
ventas["Facturacion"]=ventas["Precio_Unitario"]*ventas["Unidades"]
#print(ventas["Facturacion"])
#print(f"Total vendido: ${ventas["Facturacion"].sum()}")

ventas=ventas.merge(negocios,on="Negocio",how="left")
#print(ventas)
print("\n=== Facturación por barrio ===")
por_barrio=ventas.groupby("Barrio")["Facturacion"].sum()
print(por_barrio.to_frame())
# === GRAFICO ===
#plt.pie(por_barrio,labels=por_barrio.index,autopct="%1.1f%%")
#plt.show()
plt.figure(figsize=(10,6))
por_barrio.plot(kind='bar',color='purple',edgecolor='pink')
plt.title("Facturación por barrio",fontsize=10,fontweight='bold')
plt.xlabel("Barrio",fontsize=10)
plt.ylabel("Facturación total",fontsize=10)
plt.xticks()
plt.show()