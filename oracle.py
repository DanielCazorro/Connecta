from enum import Enum, auto
from copy import deepcopy


class ColumnClassification(Enum):
    FULL = -1   # imposible
    MAYBE = 1   # indeseable
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
        recommentation = super().get_recommendation(board, index, player)
        if recommentation.classification == ColumnClassification.MAYBE:
            # se puede mejorar
            recommentation = self._is_winning_move(board, index, player)
        return recommentation
    
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