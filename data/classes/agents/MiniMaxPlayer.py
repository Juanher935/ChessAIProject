# /* MiniMaxPlayer.py
# 14:35 For simple MinMax algorithm Example in
# https://www.youtube.com/watch?v=IDx9iWqDwZE&list=PLBwF487qi8MGU81nDGaeNE1EnNEPYWKY_&index=12&ab_channel=EddieSharick%28Eddie%29

import random

from data.classes.Square import Square
from data.classes.Board import Board
from data.classes.agents.ChessAgent import ChessAgent

# Evaluates the Board by reading each piece on the board and calculating the score total
# Need to implement Dynamic change for White to Black piece player "clicked_square.occupying_piece.color == board.turn"
# or "self.color" Might check color
def evaluate(board):
    piece_values = {
        'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 0
    }
    score = 0
    for row in board.config:
        for piece in row:
            if piece:
                value = piece_values[piece[1]]
                score += value if piece[0] == 'w' else -value
    return score


def minimax(board, depth, color, maximizingPlayer):
    if depth == 0 or board.is_in_checkmate(color):
        return evaluate(board)

    possible_moves: list[tuple[Square, Square]] = []
    for square in board.squares:
        if square.occupying_piece != None \
                and square.occupying_piece.color == color:
            for target in square.occupying_piece.get_valid_moves(board):
                possible_moves.append((square, target))

    if maximizingPlayer:
        max_value = float('-inf')
        for move in possible_moves:
            new_board = board.simulate_move(move)
            eval_value = minimax(new_board, depth - 1, color, False)
            max_value = max(max_value, eval_value)
        return max_value
    else:
        min_value = float('inf')
        for move in possible_moves:
            new_board = board.simulate_move(move)
            eval_value = minimax(new_board, depth - 1, color, True)
            min_value = min(min_value, eval_value)
        return min_value
        # minPlayer


class MiniMaxPlayer(ChessAgent):

    def choose_action(self, board: Board):
        piece_color = self.color
        best_move = None
        depth = 1
        best_value = float('-inf') if piece_color == 'white' else float('inf')

        possible_moves = []
        for square in board.squares:
            if square.occupying_piece and square.occupying_piece.color == piece_color:
                for target in square.occupying_piece.get_valid_moves(board):
                    possible_moves.append((square, target))

        # Evaluate each move using the minimax algorithm
        for move in possible_moves:
            new_board = board.simulate_move(move)
            eval_value = minimax(new_board, depth - 1, color=piece_color, maximizingPlayer=False)

            # Update the best move based on evaluation score
            if piece_color == 'white':
                if eval_value > best_value:
                    best_value = eval_value
                    best_move = move
            else:
                if eval_value < best_value:
                    best_value = eval_value
                    best_move = move

        # If no best move is found, choose a random move
        # if best_move:
        #     return best_move
        # else:
        #     return random.choice(possible_moves) if possible_moves else None
        return best_move
