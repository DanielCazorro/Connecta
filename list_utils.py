def find_one(list, needle):
    """
    Devuelve True si encuentar una o más ocurencias de needle en list
    """
    # inicializamos el bool que representa la condicion de haber encontrado o no el indice
    found = False
    index = 0
    # mientras no encontramos o hayamos terminado con la lista
    while not found and index < len(list):
        # miramos a ver si está en la posición actual y actualizamos la condición
        if needle == list[index]:
            found = True
        # avanzamos al siguiente elemento
        index = index + 1

    # devolvemos si hemos encontrado o no
    return found


def find_n(list, needle, n):
    """
    Devuelve True si en list hay n o más ocurrencias de needle
    False is hay menos o si n < 0
    """
    # si n >= 0...
    if n >= 0:
        # Inicializamos el índice y el contador
        index = 0
        count = 0

        # mientras no hayamos encontrado a lelemento n veces o no hayamos terminado la lista...
        while count < n and index < len(list):
            # si lo encontramos, actualizamos el contador
            if needle == list[index]:
                count = count + 1

            # avanzamos al siguiente elemento
            index = index + 1

        # devolvemos el resultado de comparar el contador con n
        return count >= n

    else:
        return False
