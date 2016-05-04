from random import randint


def randomHeuristic(state):
    return randint(0, 100)


def columnsHeuristic(state):
    board = state.board
    moves = legal_moves(state)
    he = 0
    for move in moves:
        x, y = move
        y -= 1
        while board.get((x, y), '.') == "X":
            y -= 1
            he += 50

        x, y = move
        y -= 1
        while board.get((x, y), '.') == "O":
            y -= 1
            he -= 25

        x, y = move
        he += (7-y)*50
    return he


def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
