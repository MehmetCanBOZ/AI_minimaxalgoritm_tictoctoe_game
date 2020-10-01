"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count=0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0:
        return O
    return X




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionss = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actionss.add((i, j))
    return actionss

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy
    if action not in actions(board):
        raise ValueError

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(new_board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_board = [[(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]]

    for combination in winner_board:
        count_x = 0
        count_o = 0
        for i, j in combination:
            if board[i][j] == X:
                count_x += 1
            if board[i][j] == O:
                count_o += 1
        if count_x == 3:
            return X
        if count_o == 3:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board)==X or winner(board)==O:
        return True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0


def minimax(board):

    ply = player(board)

    # If empty board is provided as input, return corner.
    if board == [[EMPTY] * 3] * 3:
        return (0, 0)

    if ply == X:
        v = float("-inf")
        selected_action = None
        for action in actions(board):
            minValueResult = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                selected_action = action
    elif ply == O:
        v = float("inf")
        selected_action = None
        for action in actions(board):
            maxValueResult = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                selected_action = action

    return selected_action


def maxValue(board):
    v = float("-inf")
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v


def minValue(board):
    v = float("inf")
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v

