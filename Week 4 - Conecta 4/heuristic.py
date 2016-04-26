from random import randint


def randomHeuristic(state):
    return randint(0, 100)


def posibles4EnRaya(state):
    libres = state.moves
    board = state.board
    lista = []
    for hueco in board:
        if board.get(hueco) == "X":
            lista.append(compute_utility(board, hueco, "X"))
    return sum(lista)


def compute_utility(board, move, player):
    "If X wins with this move, return 1; if O return -1; else return 0."
    lista = [0, 0, 0, 0]
    lista[0] = k_in_row(board, move, player, (0, 1))  # comprobar columna
    lista[1] = k_in_row(board, move, player, (1, 0))  # comprobar fila
    lista[2] = k_in_row(board, move, player, (1, -1))  # comprobar diagonal izquieda
    lista[3] = k_in_row(board, move, player, (1, 1))  # comprobar diagonal derecha

    return sum(lista)


def k_in_row(board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y), '.') == player:
        n += 1
        x, y = x + delta_x, y + delta_y

    x, y = move
    while board.get((x, y), '.') == player:
        n += 1
        x, y = x - delta_x, y - delta_y

    n -= 1  # Because we counted move itself twice
    if n == 4:
        return 1000
    return n


def avg(lista):
    return sum(lista) / float(len(lista))
