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
    he = comprobarDiagonalesIzquierdaArriba(board, he, move, player, -1, 1)
    he = comprobarDiagonalesIzquierdaAbajo(board, he, move, player, 1, -1)
    he = comprobarDiagonalesDerechaArriba(board, he, move, player, 1, 1)
    he = comprobarDiagonalesDerechaAbajo(board, he, move, player, -1, -1)
    return he


def comprobarDiagonalesIzquierdaArriba(board, he, move, player, desplazamientoX, desplazamientoY):
    # Diagonales
    # Izquierdea arriba
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
        x -= 1
        y += 1
    return he


def comprobarDiagonalesIzquierdaAbajo(board, he, move, player, desplazamientoX, desplazamientoY):
    # Izquierda abajo
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
        x += 1
        y -= 1
    return he


def comprobarDiagonalesDerechaArriba(board, he, move, player, desplazamientoX, desplazamientoY):
    # Derecha arriba
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
        x += 1
        y += 1
    return he


def comprobarDiagonalesDerechaAbajo(board, he, move, player, desplazamientoX, desplazamientoY):
    # Derecha abajo
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
        x -= 1
        y -= 1
    return he


def comprobarColumnas(board, he, move, player):
    he = comprobarColumnasAbajo(board, he, move, player)
    he = comprobarColumnasArriba(board, he, move, player)
    return he


def comprobarColumnasAbajo(board, he, move, player):
    # Columnas
    # Abajo
    x, y = move
    y -= 1
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
        y -= 1
    return he


def comprobarColumnasArriba(board, he, move, player):
    # Arriba
    x, y = move
    y += 1
    count = 0
    while y < 7:
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
        y += 1

    return he


def comprobarFilas(board, he, move, player):
    he = comprobarFilasIzquierda(board, he, move, player)
    he = comprobarFilasDerecha(board, he, move, player)
    return he


def comprobarFilasIzquierda(board, he, move, player):
    # Filas
    # Izquierda
    x, y = move
    x -= 1
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
        x -= 1
        count += 1
    return he


def comprobarFilasDerecha(board, he, move, player):
    # Derecha
    x, y = move
    x += 1
    count = 0
    while x < 8:
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
        x += 1
        count += 1
    return he

def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
