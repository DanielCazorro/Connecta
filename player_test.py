from oracle import BaseOracle
from player import Player
from square_board import SquareBoard


def test_play():
    """
    Comprobamos que se juega en la primera columna disponible
    """

    before = SquareBoard.fromList([[None, None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])

    after = SquareBoard.fromList([['x', None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])

    player = Player('Chip', 'x', oracle=BaseOracle())

    player.play(before)
    assert before == after
