# historia de usuario es un requerimiento de la app
# se desglosa en dif. tareas técnicas
# HU 001: Como usuario de la aplicación quiero que se clasifique cualquier número entero según sea múltiplo de 3, de 5, 
#        de ambos o de ninguno para que el juego muestre la respuesta correcta.

def fizzbuzz(num):
#si son multiplos de 3 el resto es 0
# puede ser true o falso
    if num%3==0 and num%5==0:
        return "fizzbuzz"
    if num==0:
        return "fizzbuzz"
    if num%3==0:
        return "fizz"
    if num%5==0:
        return "buzz"
# num es una variable llamado parametro
# devuelve un int, si se pone str(num) lo devuelve como string
    return num

#ej fizzbuzz(18) --> "fizz" (3) [string]
# fizzbuzz(10) --> "buzz" (5) [string]
# fizzbuzz(30) --> "fizzbuzz" (3,5) [string]
# fizzbuzz(8) --> 8 [int]
# fizzbuzz(0) --> 0 [int] con el nuevo if al principio
# bug en producción = no hubo testing antes del lanzamiento
# print(fizzbuzz(15)) = lee el codigo de abajo hacia arriba entonces devuelve "fizz"