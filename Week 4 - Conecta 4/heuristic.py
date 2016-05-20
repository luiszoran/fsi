from random import randint


def randomHeuristic(state):
    return randint(0, 100)


def heuristic(state):
    hePlayerX = calculateHeuristic(state, "X")
    hePlayerO = calculateHeuristic(state, "O")
    return hePlayerX - hePlayerO


def calculateHeuristic(state, player):
    board = state.board
    moves = legal_moves(state)
    he = 0
    for move in moves:
        # Comprobar Filas
        he += comprobarLinea(board, move, player, -1, 0)
        he += comprobarLinea(board, move, player, 1, 0)
        # Comprobar columnas
        he += comprobarLinea(board, move, player, 0, -1)
        he += comprobarLinea(board, move, player, 0, 1)
        # Comprobar diagonales
        he += comprobarLinea(board, move, player, -1, 1)
        he += comprobarLinea(board, move, player, 1, -1)
        he += comprobarLinea(board, move, player, 1, 1)
        he += comprobarLinea(board, move, player, -1, -1)
    return he


def comprobarLinea(board, move, player, desplazamientoX, desplazamientoY):
    he = 0
    x, y = move
    x += desplazamientoX
    y += desplazamientoY
    count = 0
    inRow = True
    while 0 < y < 7 and 0 < x < 8:
        if board.get((x, y), '.') == player:
            he += 50
            if inRow:
                count += 1
        elif board.get((x, y), '.') == ".":
            he += 25
            inRow = False
        else:
            break
        x += desplazamientoX
        y += desplazamientoY
    if count == 4:
        he += 1000000
    else:
        he += 10**count
    return he


def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
