from fizzbuzz import fizzbuzz

# funcion: def nomnbre ():
def procesar_archivo():
    resultados=[]
    with open("numeros.txt",encoding="utf-8") as archivo:
        for linea in archivo:
            numero=int(linea)
            resultados.append(fizzbuzz(numero))
    return resultados
print(procesar_archivo())