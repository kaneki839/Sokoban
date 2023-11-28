from game_settings import *
import copy


def board_print(board):
    for setting in board:
        print(" ".join(setting))


def game_won(board):
    for row in board:
        for col in row:
            if col == BOX_NS or col == TARGET:
                return False
    return True


def find_sprite_position(board):
    for row_b in range(len(board)):
        for col_b in range(len(board[row_b])):
            if board[row_b][col_b] in [SPRITE, SPRITE_T]:  # find sprite
                return row_b, col_b


def move(dir, row, col):
    if dir == "w":
        new_rows = [row - 1, row - 2]
        return new_rows, col
    elif dir == "s":
        new_rows = [row + 1, row + 2]
        return new_rows, col
    elif dir == "a":
        new_cols = [col - 1, col - 2]
        return row, new_cols
    elif dir == "d":
        new_cols = [col + 1, col + 2]
        return row, new_cols


if __name__ == "__main__":
    reset_board = copy.deepcopy(board)
    board_print(board)
    user_input = input()

    while True:
        while user_input not in CONTROLS:
            print("\nenter a valid move:", end="")
            user_input = input()

        if user_input == " ":
            board = copy.deepcopy(reset_board)
        elif user_input == "q":
            print()
            print("Goodbye")
            break

        try:
            row, col = find_sprite_position(board)
            new_rows, new_cols = move(user_input, row, col)
        except TypeError:
            pass

        if user_input in ["w", "s"]:  # move up or down
            if row != 0:
                if board[new_rows[0]][col] == EMPTY:  # if front is empty
                    board[new_rows[0]][col] = SPRITE
                    if board[row][col] == SPRITE_T:
                        board[row][col] = TARGET
                    else:
                        board[row][col] = EMPTY
                elif board[new_rows[0]][col] == BOX_NS:  # if front is unsatisfied box
                    if new_rows[1] >= 0:
                        if board[new_rows[1]][col] == EMPTY:
                            board[new_rows[1]][col] = BOX_NS
                            board[new_rows[0]][col] = SPRITE
                            if board[row][col] == SPRITE_T:
                                board[row][col] = TARGET
                            else:
                                board[row][col] = EMPTY
                        elif board[new_rows[1]][col] == TARGET:
                            board[new_rows[1]][col] = BOX_S
                            board[new_rows[0]][col] = SPRITE
                            if board[row][col] == SPRITE_T:
                                board[row][col] = TARGET
                            else:
                                board[row][col] = EMPTY
                        elif (
                            board[new_rows[1]][col] == BOX_NS
                            or board[new_rows[1]][col] == BOX_S
                        ):
                            board[row][col] = SPRITE
                        elif board[new_rows[1]][col] == WALL:
                            board[row][col] = SPRITE
                elif board[new_rows[0]][col] == TARGET:  # if front is target
                    board[new_rows[0]][col] = SPRITE_T
                    board[row][col] = EMPTY
                elif board[new_rows[0]][col] == BOX_S:  # if front is satisfied box
                    if board[new_rows[1]][col] == EMPTY:
                        board[new_rows[1]][col] = BOX_NS
                        board[new_rows[0]][col] = SPRITE_T
                        board[row][col] = EMPTY
                    elif board[new_rows[1]][col] == TARGET:
                        board[new_rows[1]][col] = BOX_S
                        board[new_rows[0]][col] = SPRITE_T
                        board[row][col] = TARGET
                    elif board[new_rows[1]][col] == WALL:
                        board[row][col] = SPRITE
            else:
                board[row][col] = SPRITE

        elif user_input in ["a", "d"]:  # movement left or right
            if col != 0:
                if board[row][new_cols[0]] == EMPTY:  # if front is empty
                    board[row][new_cols[0]] = SPRITE
                    if board[row][col] == SPRITE_T:
                        board[row][col] = TARGET
                    else:
                        board[row][col] = EMPTY
                elif board[row][new_cols[0]] == BOX_NS:  # if front is unsatisfied box
                    if new_cols[1] >= 0:
                        if board[row][new_cols[1]] == EMPTY:
                            board[row][new_cols[1]] = BOX_NS
                            board[row][new_cols[0]] = SPRITE
                            if board[row][col] == SPRITE_T:
                                board[row][col] = TARGET
                            else:
                                board[row][col] = EMPTY
                        elif board[row][new_cols[1]] == TARGET:
                            board[row][new_cols[1]] = BOX_S
                            board[row][new_cols[0]] = SPRITE
                            if board[row][col] == SPRITE_T:
                                board[row][col] = TARGET
                            else:
                                board[row][col] = EMPTY
                        elif (
                            board[row][new_cols[1]] == BOX_NS
                            or board[row][new_cols[1]] == BOX_S
                        ):
                            board[row][col] = SPRITE
                        elif board[row][new_cols[1]] == WALL:
                            board[row][col] = SPRITE
                elif board[row][new_cols[0]] == TARGET:  # if front is target
                    board[row][new_cols[0]] = SPRITE_T
                    board[row][col] = EMPTY
                elif board[row][new_cols[0]] == BOX_S:  # if front is satisfied box
                    if board[row][new_cols[1]] == EMPTY:
                        board[row][new_cols[1]] = BOX_NS
                        board[row][new_cols[0]] = SPRITE_T
                        board[row][col] = EMPTY
                    elif board[row][new_cols[1]] == TARGET:
                        board[row][new_cols[1]] = BOX_S
                        board[row][new_cols[0]] = SPRITE_T
                        board[row][col] = TARGET
                    elif board[row][new_cols[1]] == WALL:
                        board[row][col] = SPRITE
            else:
                board[row][col] = SPRITE

        print()
        board_print(board)
        if game_won(board):
            print("You Win!")
            break
        user_input = input()
