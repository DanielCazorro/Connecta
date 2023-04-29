from list_utils import find_streak
from settings import BOARD_LENGTH, VICTORY_STRIKE


class LinearBoard():
    """
    Clase que representa un tablero de una sola columna
    x un jugador
    o otro jugador
    None un espacio vacío
    """

    @classmethod
    def fromList(cls, list):
        board = cls()
        board._colum = list
        return board

    def __init__(self):
        """
        Una lista de None
        """
        self._colum = [None for i in range(BOARD_LENGTH)]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._colum == other._colum

    def __hash__(self):
        return hash(self._colum)

    def add(self, char):
        """
        Juega en la primera posición disponible
        """
        # siempre y cuando no esté lleno...
        if not self.is_full():
            # buscamos la priemra posición libre (None)
            i = self._colum.index(None)
            # lo sustituimos por un char
            self._colum[i] = char

    def is_full(self):
        return self._colum[-1] != None

    def is_victory(self, char):
        return find_streak(self._colum, char, VICTORY_STRIKE)

    def is_tie(self, char1, char2):
        """
        no hay victoria ni de char1 ni de char2
        """
        return (self.is_victory('x') == False) and (self.is_victory('o') == False)
