def reducir_a_un_digito(numero):
    while numero >= 10:
        numero = sum(int(digito) for digito in str(numero))
    return numero

# Ejemplos de uso:
entrada = input("Introduce un número o una fecha (solo números): ")
if entrada.isdigit():
    resultado = reducir_a_un_digito(int(entrada))
    print(f"El número reducido a un dígito es: {resultado}")
else:
    print("Por favor, introduce solo números.")
