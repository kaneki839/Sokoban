from game_settings import *
import copy

def board_print(board):
    for setting in board:
        print(' '.join(setting))

def game_won(board):
    """Returns False is not won; True if won"""
    for row in board:   
        for col in row:
            if col == BOX_NS or col == TARGET:
                return False
    return True

reset_board = copy.deepcopy(board)
board_print(board)
user_input = input()

while True:
    while user_input not in CONTROLS:
        print('\nenter a valid move:', end= '')    
        user_input = input()
    
    if user_input == ' ':
        board = copy.deepcopy(reset_board)
    elif user_input == 'q':
        print()
        print('Goodbye')
        break
    
    for row_b in range(len(board)):
        for col_b in range(len(board[row_b])):
            if board[row_b][col_b] == SPRITE: # find sprite
                row = row_b
                col = col_b
            elif board[row_b][col_b] == SPRITE_T:
                row = row_b
                col = col_b
    if user_input == 'w': # movement for w(up)
        if row != 0:
            if board[row - 1][col] == EMPTY: # if front is empty
                board[row - 1][col] = SPRITE
                if board[row][col] == SPRITE_T:
                    board[row][col] = TARGET
                else:
                    board[row][col] = EMPTY
            elif board[row - 1][col] == BOX_NS: # if front is unsatisfied box
                if row - 2 >= 0: 
                    if board[row - 2][col] == EMPTY:                                     
                        board[row - 2][col] = BOX_NS
                        board[row - 1][col] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row - 2][col] == TARGET:
                        board[row - 2][col] = BOX_S
                        board[row - 1][col] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row - 2][col] == BOX_NS or board[row - 2][col] == BOX_S:
                        board[row][col] = SPRITE
                    elif board[row - 2][col] == WALL:
                        board[row][col] = SPRITE
            elif board[row - 1][col] == TARGET: # if front is target
                board[row - 1][col] = SPRITE_T
                board[row][col] = EMPTY
            elif board[row - 1][col] == BOX_S: # if front is satisfied box
                if board[row - 2][col] == EMPTY:
                    board[row - 2][col] = BOX_NS
                    board[row - 1][col] = SPRITE_T
                    board[row][col] = EMPTY
                elif board[row - 2][col] == TARGET:
                    board[row - 2][col] = BOX_S
                    board[row - 1][col] = SPRITE_T
                    board[row][col] = TARGET
                elif board[row - 2][col] == WALL:
                    board[row][col] = SPRITE
        else:
            board[row][col] = SPRITE
    elif user_input == 's': # movement for s(down)
        if row != 0:
            if board[row + 1][col] == EMPTY: # if front is empty
                board[row + 1][col] = SPRITE
                if board[row][col] == SPRITE_T:
                    board[row][col] = TARGET
                else:
                    board[row][col] = EMPTY
            elif board[row + 1][col] == BOX_NS: # if front is unsatisfied box
                if row + 2 >= 0: 
                    if board[row + 2][col] == EMPTY:                                     
                        board[row + 2][col] = BOX_NS
                        board[row + 1][col] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row + 2][col] == TARGET:
                        board[row + 2][col] = BOX_S
                        board[row + 1][col] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row + 2][col] == BOX_NS or board[row + 2][col] == BOX_S:
                        board[row][col] = SPRITE
                    elif board[row + 2][col] == WALL:
                        board[row][col] = SPRITE
            elif board[row + 1][col] == TARGET: # if front is target
                board[row + 1][col] = SPRITE_T
                board[row][col] = EMPTY
            elif board[row + 1][col] == BOX_S:  # if front is satisfied box
                if board[row + 2][col] == EMPTY:
                    board[row + 2][col] = BOX_NS
                    board[row + 1][col] = SPRITE_T
                    board[row][col] = EMPTY
                elif board[row + 2][col] == TARGET:
                    board[row + 2][col] = BOX_S
                    board[row + 1][col] = SPRITE_T
                    board[row][col] = TARGET
                elif board[row + 2][col] == WALL:
                    board[row][col] = SPRITE
        else:
            board[row][col] = SPRITE
    elif user_input == 'a': # movement for a(left)
        if col != 0:
            if board[row][col - 1] == EMPTY: # if front is empty
                board[row][col - 1] = SPRITE
                if board[row][col] == SPRITE_T:
                    board[row][col] = TARGET
                else:
                    board[row][col] = EMPTY
            elif board[row][col - 1] == BOX_NS: # if front is unsatisfied box
                if col - 2 >= 0: 
                    if board[row][col - 2] == EMPTY:                                     
                        board[row][col - 2] = BOX_NS
                        board[row][col - 1] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row][col - 2] == TARGET:
                        board[row][col - 2] = BOX_S
                        board[row][col - 1] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row][col - 2] == BOX_NS or board[row][col - 2] == BOX_S:
                        board[row][col] = SPRITE
                    elif board[row][col - 2] == WALL:
                        board[row][col] = SPRITE
            elif board[row][col - 1] == TARGET: # if front is target
                board[row][col - 1] = SPRITE_T
                board[row][col] = EMPTY
            elif board[row][col - 1] == BOX_S: # if front is satisfied box
                if board[row][col - 2] == EMPTY:
                    board[row][col - 2] = BOX_NS
                    board[row][col - 1] = SPRITE_T
                    board[row][col] = EMPTY
                elif board[row][col - 2] == TARGET:
                    board[row][col - 2] = BOX_S
                    board[row][col - 1] = SPRITE_T
                    board[row][col] = TARGET
                elif board[row][col - 2] == WALL:
                    board[row][col] = SPRITE
        else:
            board[row][col] = SPRITE
    elif user_input == 'd': # movement for d(right)
        if col != 0:
            if board[row][col + 1] == EMPTY: # if front is empty
                board[row][col + 1] = SPRITE
                if board[row][col] == SPRITE_T:
                    board[row][col] = TARGET
                else:
                    board[row][col] = EMPTY
            elif board[row][col + 1] == BOX_NS: # if front is unsatisfied box
                if col + 2 >= 0: 
                    if board[row][col + 2] == EMPTY:                                     
                        board[row][col + 2] = BOX_NS
                        board[row][col + 1] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row][col + 2] == TARGET:
                        board[row][col + 2] = BOX_S
                        board[row][col + 1] = SPRITE
                        if board[row][col] == SPRITE_T:
                            board[row][col] = TARGET
                        else:
                            board[row][col] = EMPTY
                    elif board[row][col + 2] == BOX_NS or board[row][col + 2] == BOX_S:
                        board[row][col] = SPRITE
                    elif board[row][col + 2] == WALL:
                        board[row][col] = SPRITE
            elif board[row][col + 1] == TARGET: # if front is target
                board[row][col + 1] = SPRITE_T
                board[row][col] = EMPTY
            elif board[row][col + 1] == BOX_S:  # if front is satisfied box
                if board[row][col + 2] == EMPTY:
                    board[row][col + 2] = BOX_NS
                    board[row][col + 1] = SPRITE_T
                    board[row][col] = EMPTY
                elif board[row][col + 2] == TARGET:
                    board[row][col + 2] = BOX_S
                    board[row][col + 1] = SPRITE_T
                    board[row][col] = TARGET
                elif board[row][col + 2] == WALL:
                    board[row][col] = SPRITE
        else:
            board[row][col] = SPRITE
    print()
    board_print(board)
    if game_won(board):
        print('You Win!')
        break
    user_input = input()