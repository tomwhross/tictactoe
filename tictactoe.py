"""
Tic Tac Toe Player
"""
import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    # return [[EMPTY, X, O], [O, X, X], [EMPTY, EMPTY, O]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if board == initial_state():
        return X

    x_count = 0
    o_count = 0

    for row in board:
        for cell in row:
            if cell is X:
                x_count += 1
            if cell is O:
                o_count += 1

    if x_count > o_count:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell is EMPTY:
                possible_actions.add((row_index, cell_index))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    resulting_board = deepcopy(board)

    resulting_board[action[0]][action[-1]] = turn

    return resulting_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for potential_winner in [X, O]:
        # top row
        if (
            board[0][0] is potential_winner
            and board[0][1] is potential_winner
            and board[0][2] is potential_winner
        ):
            return potential_winner

        # middle row
        if (
            board[1][0] is potential_winner
            and board[1][1] is potential_winner
            and board[1][2] is potential_winner
        ):
            return potential_winner

        # bottom row
        if (
            board[2][0] is potential_winner
            and board[2][1] is potential_winner
            and board[2][2] is potential_winner
        ):
            return potential_winner

        # left column
        if (
            board[0][0] is potential_winner
            and board[1][0] is potential_winner
            and board[2][0] is potential_winner
        ):
            return potential_winner

        # middle column
        if (
            board[0][1] is potential_winner
            and board[1][1] is potential_winner
            and board[2][1] is potential_winner
        ):
            return potential_winner

        # right column
        if (
            board[0][2] is potential_winner
            and board[1][2] is potential_winner
            and board[2][2] is potential_winner
        ):
            return potential_winner

        # diagonal from top left
        if (
            board[0][0] is potential_winner
            and board[1][1] is potential_winner
            and board[2][2] is potential_winner
        ):
            return potential_winner

        # diagonal from top right
        if (
            board[0][2] is potential_winner
            and board[1][1] is potential_winner
            and board[2][0] is potential_winner
        ):
            return potential_winner

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if board is initial_state():
        return False

    if winner(board):
        return True

    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # import pdb

    # pdb.set_trace()

    if winner(board) is X:
        return 1

    if winner(board) is O:
        return -1

    return 0


def max_value(board):
    """
    Returns a state with the highest possible utility
    """

    if terminal(board):
        return utility(board)

    value = -math.inf

    for action in actions(board):
        action_result = result(board, action)
        action_value = min_value(action_result)
        value = max(value, action_value)

    return value


def min_value(board):
    """
    Returns a state with the lowest possible utility
    """

    if terminal(board):
        return utility(board)

    value = math.inf

    for action in actions(board):
        action_result = result(board, action)
        action_value = max_value(action_result)
        value = min(value, action_value)

    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    # list orders are persistent in python
    # so two lists built together map to each other ordinally
    possible_actions = list(actions(board))
    minmax_values = []

    if player(board) is X:
        # if board == initial_state():
        #     return (0, 0)
        # import pdb

        # pdb.set_trace()
        for action in possible_actions:
            action_result = result(board, action)
            # x is the max player, but we've already made the first move
            # so we're calling min during X's turn
            value = min_value(action_result)

            minmax_values.append(value)

        print(possible_actions)
        print(minmax_values)

        return possible_actions[minmax_values.index(max(minmax_values))]

    if player(board) is O:

        for action in possible_actions:
            action_result = result(board, action)
            value = max_value(action_result)
            minmax_values.append(value)

        print(possible_actions)
        print(minmax_values)

        return possible_actions[minmax_values.index(min(minmax_values))]

    return None
