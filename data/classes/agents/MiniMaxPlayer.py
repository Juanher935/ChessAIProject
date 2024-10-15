# /* MiniMaxPlayer.py

import random

from data.classes.Square import Square
from data.classes.Board import Board
from data.classes.agents.ChessAgent import ChessAgent

class MiniMaxPlayer(ChessAgent):
    def choose_action(self, board: Board):
        possible_moves: list[tuple[Square, Square]] = []

        if len(possible_moves) < 1:
            return False
        return random.choice(possible_moves)
