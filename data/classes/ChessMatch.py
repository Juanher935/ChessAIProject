import pygame
import time
import matplotlib.pyplot as plt
import numpy as np

from data.classes.Board import Board
from data.classes.agents.ChessAgent import ChessAgent

def chess_match(white_player: ChessAgent, black_player: ChessAgent):
    assert(white_player.color == 'white')
    assert(black_player.color == 'black')
    pygame.init()
    WINDOW_SIZE = (600, 600)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = Board(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
    agents: list[ChessAgent] = [white_player, black_player]
    i: int = 0
    moves_count: int = 0

    # Run the main game loop
    running = True
    while running:
        chosen_action = agents[i].choose_action(board)
        i = (i + 1) % len(agents)
        moves_count += 1
        if chosen_action == False or moves_count > 1000:
            print('Players draw!')
            running = False
        elif not board.handle_move(*chosen_action):
            print("Invalid move!")
        elif board.is_in_checkmate(board.turn):
            if board.turn == 'white':
                print('Black wins!')
            else:
                print('White wins!')
            running = False
        board.draw()

    # Allow the player to view the result
    viewing = True
    while viewing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                viewing = False

def game_tracker_100(white_player: ChessAgent, black_player: ChessAgent):
    total_games = 3
    move_times = []
    outcomes = []
    average_move_times = []

    for game_num in range(total_games):
        # pygame.init()
        # WINDOW_SIZE = (600, 600)
        # screen = pygame.display.set_mode(WINDOW_SIZE)
        # board = Board(screen, WINDOW_SIZE[0], WINDOW_SIZE[1])
        board = Board(None, 600, 600)
        agents: list[ChessAgent] = [white_player, black_player]
        i: int = 0
        moves_count: int = 0
        game_move_times = []

        print(f'Starting game {game_num + 1}...')
        running = True
        while running:
            # Measure time taken for each move
            start_time = time.time()
            chosen_action = agents[i].choose_action(board)
            end_time = time.time()
            move_duration = end_time - start_time
            game_move_times.append(move_duration)

            i = (i + 1) % len(agents)
            moves_count += 1

            if chosen_action == False or moves_count > 1000 or chosen_action is None:
                print('Players draw!')
                outcomes.append('Draw')
                running = False
            elif not board.handle_move(*chosen_action):
                print("Invalid move!")
            elif board.is_in_checkmate(board.turn):
                if board.turn == 'white':
                    print('Black wins!')
                    outcomes.append('Black')
                else:
                    print('White wins!')
                    outcomes.append('White')
                running = False
            #board.draw()

        # Store the average move time for this game
        average_move_time = np.mean(game_move_times)
        average_move_times.append(average_move_time)
        move_times.extend(game_move_times)
        print(f'Game {game_num + 1} completed. Average move time: {average_move_time:.4f} seconds.')

    # Plot the results
    plt.figure(figsize=(14, 6))

    # Plot average move times for each game
    plt.subplot(1, 2, 1)
    plt.plot(range(1, total_games + 1), average_move_times, label='Average Move Time per Game', color='blue',
             marker='o')
    plt.xlabel('Game Number')
    plt.ylabel('Average Move Time (s)')
    plt.title('Average Move Time Over 100 Games')
    plt.legend()

    # Plot the outcomes of each game
    plt.subplot(1, 2, 2)
    outcomes_counts = {'White': outcomes.count('White'), 'Black': outcomes.count('Black'),
                       'Draw': outcomes.count('Draw')}
    plt.bar(outcomes_counts.keys(), outcomes_counts.values(), color=['green', 'red', 'gray'])
    plt.xlabel('Outcome')
    plt.ylabel('Number of Games')
    plt.title('Game Outcomes Over 100 Games')

    # Show the plots
    plt.tight_layout()
    plt.show()