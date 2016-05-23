import games
import heuristic

#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial

def computersTurn():
    global state, player
    print "Thinking..."
    # move = games.minimax_decision(state, game)
    # move = games.alphabeta_full_search(state, game)
    move = games.alphabeta_search(state, game, d=profundidad, eval_fn=heuristic.heuristic)
    state = game.make_move(move, state)
    player = 'player'


def playersTurn():
    global col_str, coor, state, player
    col_str = raw_input("Movimiento: ")
    coor = int(str(col_str).strip())
    x = coor
    y = -1
    legal_moves = game.legal_moves(state)
    for lm in legal_moves:
        if lm[0] == x:
            y = lm[1]
    state = game.make_move((x, y), state)
    player = 'computer'


dif_str = raw_input("Elija el nivel de dificultad, Facil(1), Medio(2), Dificil(3)): ")
dif = int(str(dif_str).strip())

if dif < 1 or dif > 3:
    print "Numero incorrecto, jugando dificultad media."
    dif = 2

if dif == 1:
    profundidad = 2
elif dif == 2:
    profundidad = 4
else:
    profundidad = 6

emp_str = raw_input("Quiere empezar usted (S/N)?: ")
emp = str(emp_str).strip().lower()

if emp == "s":
    player = "player"
else:
    player = "computer"
#    move = games.alphabeta_search(state, game, eval_fn=heuristic.heuristic)


while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'player':
        playersTurn()
    else:
        computersTurn()
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
