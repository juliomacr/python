def factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

for i in range(1, 10):
    print(f"El factorial de {i} es: {factorial(i)}")