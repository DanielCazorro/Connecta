from match import Match
from oracle import BaseOracle, LearningOracle, SmartOracle
from player import HumanPlayer, Player, ReportingPlayer
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

    def __init__(self, round_type=RoundType.COMPUTER_VS_COMPUTER, match=Match(ReportingPlayer('Chip'), ReportingPlayer('Chop'))):
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
            # si hay vencedor o empate,
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
            f'\n{player.name} ({player.char}) has moved in column #{player.last_moves[0].position}\n')

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

    def _configura_by_user(self):
        """
        Le pido al usuario, los valores que él quiere para tipo de partida y nivel de dificultad
        """
        # determinar el tipo de partida (preguntando al usuario)
        self.round_type = self._get_round_type()

        # Preguntamos nivel de dificultad
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()

        # crear la partida
        self.match = self._make_match()

    def _get_difficulty_level(self):
        """
        Pregunta al usuario como de listo quiere que sea su oponente
        """
        print("""
        Choose your opponent, human:
        
        1) Bender: for clowns and wimps
        2) T-800 : you may regret it
        3) T-1000: Don't even think about it!
        """)
        while True:
            response = input('Please type 1, 2 or 3: ').strip()
            if response == '1':
                level = DifficultyLevel.LOW
                break
            elif response == '2':
                level = DifficultyLevel.MEDIUM
                break
            else:
                level = DifficultyLevel.HIGH
                break
        return level

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
        _levels = {DifficultyLevel.LOW: BaseOracle(),
                   DifficultyLevel.MEDIUM: SmartOracle(),
                   DifficultyLevel.HIGH: LearningOracle()}
        
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            # ambos jugadores robóticos
            player1 = ReportingPlayer('T-X', oracle=LearningOracle())
            player2 = ReportingPlayer('T-1000', oracle=LearningOracle())

        else:
            # ordenador vs humano
            player1 = Player('T-800', oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name=input('Enter your name, puny human: '))

        return Match(player1, player2)
