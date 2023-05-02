from match import Match
from player import HumanPlayer, Player
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
        self._start_game_loop()

    def print_logo(self):
        logo = pyfiglet.Figlet(font='stop')
        print(logo.renderText('Connecta'))

    def _start_game_loop():
        # bucle infinito
        while True:
            # obtengo el jugador de turno
            current_player = self.match.next_player
            # le hago jugar
            current_player.play(self.board)
            # muestro su jugada
            self.display_move(current_player)
            # imprimo el tablero
            self.display_board()
            # si el juego ha terminado...
            if self._is_game_over():
                # muestro resultado final
                self.display_result()
                # salgo del bucle
                break

    def display_move(self, player):
        pass

    def display_board(self):
        pass

    def display_result(self):
        pass

    def _is_game_over(self):
        pass

    def _configura_by_user(self):
        """
        Le pido al usuario, los valores que él quiere para tipo de partida y nivel de dificultad
        """
        # determinar el tipo de partida (preguntando al usuario)
        self.round_type = self._get_round_type()

        # crear la partida
        self.match = self._make_match()

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

    def _make_match(self):
        """
        Player 1 siempre robótico
        """
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            # ambos jugadores robóticos
            player1 = Player('T-X')
            player2 = Player('T-1000')

        else:
            # ordenador vs humano
            player1 = Player('T-800')
            player2 = HumanPlayer(name=input('Enter your name, puny human: '))

        return Match(player1, player2)
