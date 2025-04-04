# Escribir un programa que pregunte al usuario su edad y muestre
# por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

def printAge(age):
    for age in range(age):
        print(age + 1) 
    # end for
# end def

age= int(input("How old are you?"))
printAge(age)

