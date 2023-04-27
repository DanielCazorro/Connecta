import pytest

from square_board import *


def test_empty_board():
    board = SquareBoard()

    assert board.is_full() == False
    assert board.is_victory('o') == False
    assert board.is_victory('x') == False
