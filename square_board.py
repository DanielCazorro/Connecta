from linear_board import LinearBoard
from list_utils import displace_matrix, transpose
from settings import BOARD_LENGTH


class SquareBoard():
    """
    Representa un tablero cuadrado
    """

    @classmethod
    def fromList(cls, list_of_lists):
        """
        Transforma una lista de listas en una list de LinearBoard
        """
        board = cls()
        board._colums = list(
            map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board

    def __init__(self):
        self._colums = [LinearBoard() for _ in range(BOARD_LENGTH)]

    def is_full(self):
        """
        True si todos los LinearBoards están llenos
        """
        result = True
        for lb in self._colums:
            result = result and lb.is_full()
        return result

    def as_matrix(self):
        """
        Devuelve una representación en fromato de matriz, es decir,
        lista de listas.
        """
        return list(map(lambda x: x._colum, self._colums))

    # Detectra victorias
    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    def _any_vertical_victory(self, char):
        result = False
        for lb in self._colums:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char):
        # Transponemos _columns
        transp = transpose(self.as_matrix())
        # Creamos un tablero temporal con esa matriz transpuesta
        tmp = SquareBoard.fromList(transp)

        # comprobamos si tiene una victoria temporal
        return tmp._any_vertical_victory(char)

    def _any_rising_victory(self, char):
        return False

    def _any_sinking_victory(self, char):
        # Obtenemos las columnas como una matriz
        m = self.as_matrix()
        # la desplazamos
        d = displace_matrix(m)
        # creamos un tablero temporal con esa matriz
        tmp = SquareBoard.fromList(d)
        # averiguamos si tiene una vitroia horizontal
        return tmp._any_horizontal_victory(char)

    # Dunders
    def __repr__(self):
        return f'{self.__class__}:{self._colums}'
