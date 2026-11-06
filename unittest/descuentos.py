def descuento_producto(precio,porcentaje):
    if precio>100000:
        porcentaje=porcentaje+5
    return precio-(precio*porcentaje/100)

#print(descuento_producto(20000,10)) -> 18000
#print(descuento_producto(200000,10)) -> 170000
#print(descuento_producto(100000,10)) -> 85000

#assert descuento_producto(20000,10)==18000
#assertion error: debe ser documentado para arreglarlo
#assert descuento_producto(100000,10)==85000