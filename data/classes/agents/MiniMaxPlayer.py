# /* MiniMaxPlayer.py
# 14:35 For simple MinMax algorithm Example in
# https://www.youtube.com/watch?v=IDx9iWqDwZE&list=PLBwF487qi8MGU81nDGaeNE1EnNEPYWKY_&index=12&ab_channel=EddieSharick%28Eddie%29

import random

from data.classes.Square import Square
from data.classes.Board import Board
from data.classes.agents.ChessAgent import ChessAgent

class MiniMaxPlayer(ChessAgent):

    def evaluate(self, board):
        piece_values = {
            'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0
        }
        score = 0
        for row in board:
            for piece in row:
                if piece:
                    value = piece_values[piece[1]]
                    score += value if piece[0] == 'w' else -value
        return score

    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0:
            return self.evaluate(board)
        if maximizingPlayer:
            max_Value = float('-inf')
            pass
        else:
            pass
            # minPlayer

    def choose_action(self, board: Board):
        possible_moves: list[tuple[Square, Square]] = []

        if len(possible_moves) < 1:
            return False
        return random.choice(possible_moves)
