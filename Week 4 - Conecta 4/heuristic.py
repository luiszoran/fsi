from random import randint


def randomHeuristic(state):
    return randint(0, 100)

def columnsHeuristic(state):
    board = state.board
    h, v = 7, 6
    lista = []
    for x in range(1, h + 1):
        for y in range(v, 0, -1):
            ficha = board.get((x, y), '.')
            if ficha == ".":
                continue
            if ficha == "O":
                lista.append(-1)
                break

            if ficha == "X":
                j = y - 1
                while board.get((x, j), '.') == "X":
                    j -= 1
                lista.append((y - j) * 2)
                break
    return max(lista)