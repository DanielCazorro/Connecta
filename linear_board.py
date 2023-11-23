from list_utils import find_streak
from settings import BOARD_LENGTH, VICTORY_STRIKE

class LinearBoard():
    """
    Clase que representa un tablero de una sola columna
    x: un jugador
    o: otro jugador
    None: un espacio vacío
    """

    def __init__(self):
        """
        Inicializa el tablero con una lista de longitud BOARD_LENGTH, inicialmente vacía
        """
        self._column = [None for i in range(BOARD_LENGTH)]

    def add(self, char):
        """
        Agrega una ficha en la primera posición disponible
        """
        if not self.is_full():
            # Encuentra la primera posición libre y coloca la ficha
            i = self._column.index(None)
            self._column[i] = char

    def is_full(self):
        """
        Verifica si el tablero está lleno
        """
        return self._column[-1] != None

    def is_victory(self, char):
        """
        Verifica si hay una victoria para el jugador 'char' en el tablero
        """
        return find_streak(self._column, char, VICTORY_STRIKE)

    def is_tie(self, char1, char2):
        """
        Verifica si el juego termina en empate
        """
        return (self.is_victory(char1) == False) and (self.is_victory(char2) == False)
