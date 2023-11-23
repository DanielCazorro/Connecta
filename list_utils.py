def find_one(list, needle):
    """
    Devuelve True si encuentra una o más ocurrencias de 'needle' en 'list'
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
    Devuelve True si hay 'n' o más 'needle' consecutivos en 'list'
    """
    if n >= 0:
        index = 0
        count = 0
        streak = False

        while count < n and index < len(list):
            if needle == list[index]:
                streak = True
                count = count + 1
            else:
                streak = False
                count = 0

            index = index + 1

        return count >= n and streak
    else:
        return False