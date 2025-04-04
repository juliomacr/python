# Ejercicio 1: Encontrar un Número en una Lista Ordenada
# Dada una lista ordenada de enteros y un número objetivo, 
# implementa la función buscar_numero(lista, objetivo) que 
# devuelva el índice donde se encuentra el número. 
# Si el número no está en la lista, devuelve -1.


def buscar_numero(lista, numero):
    left, right = 0, len(lista) - 1
    
    while left <= right:
        center = (left + right) // 2
        
        if lista[center] == numero:
            return center
        
        elif lista[center] < numero:
            left = center + 1
            
        else:
            right= center -1
            
    return -1
    

    
# end def


lista = [2, 4, 7, 10, 15, 20]
print(buscar_numero(lista, 10))  # Debe devolver 3
print(buscar_numero(lista, 5))   # Debe devolver -1
print(buscar_numero(lista, 8))   # Debe devolver -1

