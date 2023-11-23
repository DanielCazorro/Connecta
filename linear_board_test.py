import pytest
from linear_board import *
from settings import BOARD_LENGTH, VICTORY_STRIKE

# Pruebas para el tablero de Conecta 4

def test_empty_board():
    # Verifica que el tablero esté vacío al inicio
    empty = LinearBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False


def test_add():
    # Verifica si el tablero se llena correctamente
    b = LinearBoard()
    for i in range(BOARD_LENGTH):
        b.add('x')
    assert b.is_full() == True


def test_victory():
    # Verifica la detección correcta de la victoria
    b = LinearBoard()
    for i in range(VICTORY_STRIKE):
        b.add('x')

    assert b.is_victory('o') == False
    assert b.is_victory('x') == True


def test_tie():
    # Verifica si el juego termina en empate
    b = LinearBoard()

    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')

    assert b.is_tie('x', 'o')


def test_add_to_full():
    # Verifica que no se pueda agregar a un tablero lleno
    full = LinearBoard()
    for i in range(BOARD_LENGTH):
        full.add('x')

    full.add('x')
    assert full.is_full()
