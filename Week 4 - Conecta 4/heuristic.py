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
        he = comprobarFilas(board, he, move, player)
        he = comprobarColumnas(board, he, move, player)
        he = comprobarDiagonales(board, he, move, player)

    return he


def comprobarDiagonales(board, he, move, player):
    # Diagonales
    # Izquierdea arriba
    x, y = move
    x -= 1
    y += 1
    while y > 0 and y < 7 and x > 0 and x < 8:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x -= 1
        y += 1

    # Izquierda abajo
    x, y = move
    x += 1
    y -= 1
    while y > 0 and y < 7 and x > 0 and x < 8:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x += 1
        y -= 1

    # Derecha arriba
    x, y = move
    x += 1
    y += 1
    while y > 0 and y < 7 and x > 0 and x < 8:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x += 1
        y += 1

    # Derecha abajo
    x, y = move
    x -= 1
    y -= 1
    while y > 0 and y < 7 and x > 0 and x < 8:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x -= 1
        y -= 1
    return he


def comprobarColumnas(board, he, move, player):
    # Columnas
    # Abajo
    x, y = move
    y -= 1
    while y > 0:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        y -= 1

    # Arriba
    x, y = move
    y += 1
    while y < 7:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        y += 1

    return he


def comprobarFilas(board, he, move, player):
    # Filas
    # Izquierda
    x, y = move
    x -= 1
    while x > 0:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x -= 1

    # Derecha
    x, y = move
    x += 1
    while x < 8:
        if board.get((x, y), '.') == player:
            he += 50
        elif board.get((x, y), '.') == ".":
            he += 25
        else:
            break
        x += 1

    return he


def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
