#pip install pandas
#pip install openpyxl
import pandas as pd 
# dataframe de pandas
nombre_planilla=input("Ingrese el nombre de la planilla")

ventas=pd.read_excel(nombre_planilla,sheet_name="Ventas")

#print(ventas.describe())
#print(ventas["Precio_Unitario"])
ventas["Facturacion"]=ventas["Precio_Unitario"]*ventas["Unidades"]
#print(ventas["Facturacion"])
#print(f"Total vendido: ${ventas["Facturacion"].sum()}")

negocios=pd.read_excel(nombre_planilla,sheet_name="Negocios")

ventas=ventas.merge(negocios,on="Negocio",how="left")
#print(ventas)
print("\n=== Facturación por barrio ===")
por_barrio=ventas.groupby("Barrio")["Facturacion"].sum()
print(por_barrio.to_frame())
