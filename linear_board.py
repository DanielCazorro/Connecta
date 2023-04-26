from settings import BOARD_LENGTH


class LinearBoard():
    """
    Clase que representa un tablero de una sola columna
    x un jugador
    o otro jugador
    None un espacio vacío
    """

    def __init__(self):
        """
        Una lista de None
        """
        self._colum = [None for i in range(BOARD_LENGTH)]

    def add(self, char):
        """
        Juega en la primera posición disponible
        """
        # buscamos la priemra posición libre (None)
        i = self._colum.index(None)
        # lo sustituimos por un char
        self._colum[i] = char

    def is_full(self):
        pass

    def is_victory(self, char):
        return False

    def is_tie(self, char1, char2):
        return False
