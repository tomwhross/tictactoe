"""
Tic Tac Toe Player

Additional sources for Alpha-Beta Pruning:
1. https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
2. https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/
3. https://www.youtube.com/watch?v=l-hh51ncgDI
"""

import math
import random
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


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

    if winner(board) is X:
        return 1

    if winner(board) is O:
        return -1

    return 0


def _minimax(board, alpha, beta):
    """
    Recursive function that returns the utility of a board
    in a terminal state.

    Alpha-Beta pruning is applied to speed up the process.
    """

    if terminal(board):
        return utility(board)

    if player(board) is X:
        max_value = -math.inf

        for action in actions(board):
            action_result = result(board, action)

            value = _minimax(action_result, alpha, beta)
            max_value = max(max_value, value)

            # pruning
            alpha = max(alpha, value)

            if beta <= alpha:
                break

        return max_value

    min_value = math.inf

    for action in actions(board):
        action_result = result(board, action)
        value = _minimax(action_result, alpha, beta)
        min_value = min(min_value, value)

        # pruning
        beta = min(beta, value)

        if beta <= alpha:
            break

    return min_value


def minimax(board):
    """
    Entrypoint for _minimax recursive function
    Returns None is board is in terminal state.

    Otherwise returns the utility of the resulting board
    and action.
    """

    if terminal(board):
        return None

    possible_actions = list(actions(board))
    random.shuffle(possible_actions)
    minmax_values = []

    if player(board) is X:
        for action in possible_actions:
            action_result = result(board, action)
            value = _minimax(action_result, -math.inf, math.inf)

            minmax_values.append(value)

        return possible_actions[minmax_values.index(max(minmax_values))]

    # O player
    for action in possible_actions:
        action_result = result(board, action)
        value = _minimax(action_result, -math.inf, math.inf)

        minmax_values.append(value)

    return possible_actions[minmax_values.index(min(minmax_values))]
