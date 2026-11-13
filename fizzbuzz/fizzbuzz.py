def fizzbuzz(num):
    #si son multiplos de 3 o 5
    if num%3==0:
        return "fizz"
    if num%5==0:
        return "buzz"
    if num%3==0 and num%5==0:
        return
    return num
#ej fizzbuzz(6) --> fizz (3)
#   fizzbuzz(10) --> buzz (5)
#   fizzbuzz(15) --> fizzbuzz (3,5)
#   fizzbuzz(8) --> 8