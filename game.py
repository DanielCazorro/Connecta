from match import Match
from player import HumanPlayer, Player
import pyfiglet
from beautifultable import BeautifulTable
from enum import Enum, auto
from settings import BOARD_LENGTH

from square_board import SquareBoard
from list_utils import reverse_matrix


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

    def _start_game_loop(self):
        # bucle infinito
        while True:
            # obtengo el juagdor de turno
            current_player = self.match.next_player
            # le hago jugar
            current_player.play(self.board)
            # muestro su jugada
            self._display_move(current_player)
            # imprimo el tablero
            self._display_board()
            # si el juego ha terminado,
            if self._has_winner_or_tie():
                # muestro el resultado final
                self._display_result()

                if self.match.is_match_over():
                    # se acabó
                    break
                else:
                    # reseteamos el board
                    self.board = SquareBoard()
                    self._display_board()

    def _display_move(self, player):
        print(
            f'\n{player.name} ({player.char} has moved in column {player.last_move})')

    def _display_board(self):
        """
        Print the board in its current state
        """

        # obtener una matriz de caracteres a partir del tablero
        matrix = self.board.as_matrix()
        matrix = reverse_matrix(matrix)

        # crear un atabla con beautifultable
        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]

        # imprimirla
        print(bt)

    def _display_result(self):
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f"\n{winner.name} ({winner.char}) wins!!!")
        else:
            print(
                f"\nA tie between {self.match.get_player('x').name} (x) and {self.match.get_player('o').name} (o)")

    def _has_winner_or_tie(self):
        """
        Game is over if there's a winner or there's a tie
        """
        winner = self.match.get_winner(self.board)
        if winner != None:
            winner.on_win()
            winner.opponent.on_lose()
            return True  # there is a winner
        elif self.board.is_full():
            return True  # tie
        else:
            return False  # the game is still on

    def _is_game_over(self):
        """
        El juego se acaba cuando hay vencedor o empate
        """
        winner = self.match._has_winner_or_tie(self.board)
        if winner != None:
            # hay un vencedor
            return True
        elif self.board.is_full:
            # empate
            return True
        else:
            return False

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
