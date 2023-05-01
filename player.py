from oracle import BaseOracle, ColumnClassification


class Player():
    """
    Juega en un tablero después de preguntar a un oráculo
    """

    def __init__(self, name,  char=None, opponent=None,   oracle=BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play(self, board):
        """
        Elige la mejor columna de aquellas que recomienda el oráculo
        """
        # obtén las recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)

        # selecciona la mejor de todas
        best = self._choose(recommendations)
        # juega en ella
        board.add(self.char, best.index)

    def _choose(self, recommendations):
        #  quitamos las no válicas
        valid = list(filter(lambda x: x.classification !=
                            ColumnClassification.FULL, recommendations))

        # pillamos la primera de las válidas
        return valid[0]

# funciones de validación de índice de columna


def _is_non_full_column(board, num):
    return not board._columns[num].is_full()


def _is_within_column_range(board, num):
    return num >= 0 and num < len(board)


def _is_int(aString):
    try:
        num = int(aString)
        return True
    except:
        return False
