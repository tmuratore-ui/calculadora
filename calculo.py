def sumar(a, b):
    return a + b
def resta(a, b ):
    return a-b
def multi(a, b):
    return a*b
def divi(a, b):
    return a/b
def potenciacion(a,b):
    return a**b
def radicacion(a,b):
    return a ** (1/b)
def modulo(a,b):
    return a % b
def porcentaje(a,b):
    return (a*100)/b
def factorial(a,b):
    if n < 0:
        return "Error: Factorial de número negativo"
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado
def promedio(lista):
    if not lista:
        return "Error: Lista vacía"
    return sum(lista) / len(lista)