from oracle import *
from square_board import SquareBoard


def test_base_oracle():
    board = SquareBoard.fromList([[None, None, None, None],
                                  ['x', 'o', 'x', 'o'],
                                  ['o', 'o', 'x', 'x'],
                                  ['o', None, None, None, ]])
    expected = [ColumnRecommendation(0, ColumnClassification.MAYBE),
                ColumnRecommendation(1, ColumnClassification.FULL),
                ColumnRecommendation(2, ColumnClassification.FULL),
                ColumnRecommendation(3, ColumnClassification.MAYBE)]

    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected
