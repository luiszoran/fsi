from random import randint
import math
import starter

def randomHeuristic(state):
    return randint(0, 100)


def memoize(function):
    memo = {}
    def helper(state):
        if str(state.board) not in memo:
            memo[str(state.board)] = function(state)
        return memo[str(state.board)]
    return helper


@memoize
def heuristic(state):
    if starter.getStarter() == "computer":
        computer = "X"
        player = "O"
    else:
        computer = "O"
        player = "X"
    hePlayerC = calculateHeuristic(state, computer)
    hePlayerP = calculateHeuristic(state, player)
    if math.isinf(hePlayerP):
        return -hePlayerP
    if math.isinf(hePlayerC):
        return hePlayerC
    return hePlayerC - hePlayerP

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
    if y > 1:
        y -= 1
    count = 0
    inRow = True
    while 0 < y < 7 and 0 < x < 8:
        if board.get((x, y), '.') == player:
            he += 50
            if inRow:
                count += 1
        elif board.get((x, y), '.') == ".":
            he += 30
            inRow = False
        else:
            break
        x += desplazamientoX
        y += desplazamientoY
    if count >= 4:
        he = float('inf')
    elif count > 0:
        he += 10**count
    return he


def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
