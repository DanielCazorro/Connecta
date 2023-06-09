def find_one(list, needle):
    """
    Devuelve True si encuentar una o más ocurencias de needle en list
    """
    return find_n(list, needle, 1)


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


def find_streak(list, needle, n):
    """
    Devuelve True si en list hay n o más needles seguidos
    False, para todo lo demás
    """
    # Si n>=0
    if n >= 0:
        # Inicializo el índice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False

        # Mientras no haya encontrado a n sguidos y la lista no se haya acabado...
        while count < n and index < len(list):
            # Si lo encuentro, activo el indicador de rachas y actualizao el contador
            if needle == list[index]:
                streak = True
                count = count + 1
            else:
                # Si no lo encuentro, desactivo el indicador de la racha y pongo a cero el contador
                streak = False
                count = 0

            # Avanzo al siguiente elemento
            index = index + 1

        # Devolvemos el resultado de comparar el contador con n SIEMPRE Y CUANDO estemos en racha
        return count >= n and streak
    else:
        # Para valores de n < 0, no tiene sentido
        return False
