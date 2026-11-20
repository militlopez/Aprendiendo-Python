def fizzbuzz(num):
    """
    Devuelve una cadena según la divisibilidad 
    del número recibido.

    Parámetros:
        num (int): número entero a evaluar.
        al poner str(num) lo devuelve como string.

    Retorna:
        str: "fizzbuzz" si num es divisible por 3 y por 5.
        str: "fizz" si num es divisible solo por 3.
        str: "buzz" si num es divisible solo por 5.
        int: "fizzbuzz" si el num es 0.
        int: el mismo número num si no es divisible por 3 ni por 5.
    """
    if num%3==0 and num%5==0:
        return "fizzbuzz"
    if num==0:
        return "fizzbuzz"
    if num%3==0:
        return "fizz"
    if num%5==0:
        return "buzz"
    return num