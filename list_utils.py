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
