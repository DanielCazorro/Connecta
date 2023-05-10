from enum import Enum, auto
from copy import deepcopy

from settings import BOARD_LENGTH
from square_board import SquareBoard


class ColumnClassification(Enum):
    FULL = -1   # imposible
    BAD = 1    # Muy indeseable
    MAYBE = 10   # indeseable
    WIN = 100   # La mejor opción: gano por narices


class ColumnRecommendation():
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    def __eq__(self, other):
        #  si son de clases distintas, pues distintos
        if not isinstance(other, self.__class__):
            return False
        #  sólo importa la clasificación
        else:
            return self.classification ==  other.classification

    def __hash__(self) -> int:
        return hash((self.index, self.classification))


class BaseOracle():

    def get_recommendation(self, board, player):
        """
        Returns a list of ColumnRecommendations
        """
        recommendations = []
        for i in range(len(board)):
            recommendations.append(
                self._get_column_recommendation(board, i, player))
        return recommendations

    def _get_column_recommendation(self, board, index, player):
        """
        Classifies a column as either FULL or MAYBE and returns an ColumnRecommendation
        """
        classification = ColumnClassification.MAYBE
        if board._columns[index].is_full():
            classification = ColumnClassification.FULL

        return ColumnRecommendation(index, classification)

class SmartOracle(BaseOracle):

    def _get_column_recommendation(self, board, index, player):
        """
        Afina la clasificación de super e intenta encontrar columnas WIN
        """
        recommentation = super()._get_column_recommendation(board, index, player)
        if recommentation.classification == ColumnClassification.MAYBE:
            # se puede mejorar
            if self._is_winning_move(board, index, player):
                recommentation.classification = ColumnClassification.WIN
            elif self._is_losing_move(board, index, player):
                recommentation.classification = ColumnClassification.BAD
        return recommentation
    
    def _is_losing_move(self, board, index, player):
        """
        Si player juega en index, ¿genera una jugada vencedora par el oponente en alguna de las demás columans
        """
        tmp = self._play_on_tmp_board(board, index, player)

        will_lose = False
        for i in range(0, BOARD_LENGTH):
            if self._is_winning_move(tmp, i, player.opponent):
                will_lose = True
                break
        return will_lose


    def _is_winning_move(self, board, index, player):
        """
        Determina si al jugar en una posición, nos llevaría a ganar de inmediato
        """
        # Hago una copia del tabler
        # Juego en ella
        tmp = self._play_on_tmp_board(board, index, player)

        # Determino si hay una victoria para player
        return tmp.is_victory(player.char)
    
    def _play_on_tmp_board(self, board, index, player):
        """
        Crea una copia del board y juega en él
        """
        tmp = deepcopy(board)

        tmp.add(player.char, index)

        # devuelvo la copia alterada
        return tmp
    
class MemoizingOracle(SmartOracle):
    """
    El método get_recommendation está ahora memoizado
    """
    def __init__(self) -> None:
        super().__init__()
        self._past_recommendations = {}

    def _make_key(self, board_code, player):
        """
        La clave debe de combinar el board y el player, de la forma más sencilla posible
        """
        return f'{board_code.raw_code}@{player.char}'

    def get_recommendation(self, board, player):
        # Creamos la clave
        key = self._make_key(board.as_code(), player)

        # Miramos en el caché: si no está, calculo y guardo en la nube
        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(board, player)

        # Devuelvo lo que está en el caché
        return self._past_recommendations[key]

class LearningOracle(MemoizingOracle):
    
    def update_to_bad(self, board_code, player, position):
        # Crear clave
        key = self._make_key(board_code, player)

        # Obtener la clasificación errónea
        recommendation = self.get_recommendation(SquareBoard.fromBoardCode(board_code, player))

        # Corregirla
        recommendation[position] = ColumnRecommendation(position, ColumnClassification.BAD)

        # Sustituirla
        self._past_recommendations[key] = recommendation
