from oracle import BaseOracle, ColumnClassification, ColumnRecommendation


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
        # Pretunto al oráculo
        (best, recommendations) = self._ask_oracle(board)

        # Juego en la mejor
        self._play_on(board, best.index)

    def _play_on(self, board, position):
        # juega en la pos
        board.add(self.char, position)

    def _ask_oracle(self, board):
        """
        Pregunta al oráculo y devuelve la mejor opción
        """
        # obtenemos la recomendaciones
        recommendations = self._oracle.get_recommendation(board, self)

        # seleccionamos la mejor
        best = self._choose(recommendations)

        return (best, recommendations)

    def _choose(self, recommendations):
        #  quitamos las no válicas
        valid = list(filter(lambda x: x.classification !=
                            ColumnClassification.FULL, recommendations))

        # pillamos la primera de las válidas
        return valid[0]


class HumanPlayer(Player):

    def __init__(self, name, char):
        super().__init__(name, char)

    def _ask_oracle(self, board):
        """
        Le pido al humano que es mi oráculo
        """
        while True:
            # Pedimos columna al humano
            raw = input('Select a column, puny human: ')
            # Verficamos que su respuesta no se auna idiotez
            if _is_int(raw) and _is_within_column_range(board, int(raw)) and _is_non_full_column(board, int(raw)):

                # Si no lo es, jugamos donde ha dicho y salimos del bucle
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)


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
