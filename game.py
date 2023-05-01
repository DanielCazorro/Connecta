from match import Match
from player import Player
import pyfiglet
from enum import Enum, auto

from square_board import SquareBoard


class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    COMPUTER_VS_HUMAN = auto()


class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Game:

    def __init__(self, round_type=RoundType.COMPUTER_VS_COMPUTER, match=Match(Player('Chip'), Player('Chop'))):
        # Guardar valores recibidos
        self.round_type = round_type
        self.match = match

        # tablero vacío sobre el que jugar
        self.board = SquareBoard()

    def start(self):
        # imprimo el nombre o logo del juego
        self.print_logo()

        # configuro la partida
        self._configura_by_user()
        # arranco el game loop
        pass

    def print_logo(self):
        logo = pyfiglet.Figlet(font='stop')
        print(logo.renderText('Connecta'))

    def _configura_by_user(self):
        """
        Le pido al usuario, los valores que él quiere para tipo de partida y nivel de dificultad
        """
        # determinar el tipo de partida (preguntando al usuario)
        self.round_type = self._get_round_type()

        # crear la partida
        self.match = self.make_match()

    def _get_round_type(self):
        """
        Preguntamos al usuario
        """
        print("""
        Select type of round:

        1) Computer vs Computer
        2) Computer vs Human
        """)

        response = ""
        while response != "1" and response != "2":
            response = input("Please type either 1 or 2: ")
        if response == "1":
            return RoundType.COMPUTER_VS_COMPUTER
        else:
            return RoundType.COMPUTER_VS_HUMAN

    def make_match(self):
        pass
