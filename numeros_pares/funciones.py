#  Uso notacion snake case
def par_impar(num):
    """
    Indica si un número entero es cero, par o impar.

    Parámetros:
        num (int): número entero a evaluar.

    Retorna:
        str: "cero" si num es 0.
        str: "par" si num es divisible por 2.
        str: "impar" en cualquier otro caso.
""" 
    if num==0:
        return "cero"
    if num%2==0:
        return "par"
    return "impar"

def lista_par_impar(lista_nums):
    lista_resultados=[]
    for numero in lista_nums:
        lista_resultados.append(par_impar(numero))
    return lista_resultados

print(lista_par_impar([2,5,7,13,8,9,25]))