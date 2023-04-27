from linear_board import LinearBoard
from settings import BOARD_LENGTH


class SquareBoard():
    """
    Representa un tablero cuadrado
    """

    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]

    def is_full(self):
        """
        True si todos los LinearBoards están llenos
        """
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result

    # Detecta victorias
    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result

    def _any_horizontal_victory(self, char):
        return False

    def _any_rising_victory(self, char):
        return False

    def _any_sinking_victory(self, char):
        return False
