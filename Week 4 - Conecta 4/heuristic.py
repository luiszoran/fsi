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
        he += comprobarFilas(board, move, player)
        he += comprobarColumnas(board, move, player)
        he += comprobarDiagonales(board, move, player)
    return he


def comprobarFilas(board, move, player):
    he = 0
    he += comprobarFila(board, move, player, -1)
    he += comprobarFila(board, move, player, 1)
    return he


def comprobarFila(board, move, player, desplazamiento):
    he = 0
    x, y = move
    x += desplazamiento
    count = 0
    while x > 0:
        if count == 4:
            he += 5000
            return he
        if board.get((x, y), '.') == player:
            he += 50
            count += 1
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x += desplazamiento
        count += 1
    return he


def comprobarColumnas(board, move, player):
    he = 0
    he += comprobarColumna(board, move, player, -1)
    he += comprobarColumna(board, move, player, 1)
    return he


def comprobarColumna(board, move, player, desplazamiento):
    he = 0
    x, y = move
    y += desplazamiento
    count = 0
    while y > 0:
        if count == 4:
            he += 5000
            return he
        if board.get((x, y), '.') == player:
            he += 50
            count += 1
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        y += desplazamiento
    return he


def comprobarDiagonales(board, move, player):
    he = 0
    he += comprobarDiagonal(board, move, player, -1, 1)
    he += comprobarDiagonal(board, move, player, 1, -1)
    he += comprobarDiagonal(board, move, player, 1, 1)
    he += comprobarDiagonal(board, move, player, -1, -1)
    return he


def comprobarDiagonal(board, move, player, desplazamientoX, desplazamientoY):
    he = 0
    x, y = move
    x += desplazamientoX
    y += desplazamientoY
    count = 0
    while y > 0 and y < 7 and x > 0 and x < 8:
        if count == 4:
            he += 5000
            return he
        if board.get((x, y), '.') == player:
            he += 50
            count += 1
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x += desplazamientoX
        y += desplazamientoY
    return he

def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
