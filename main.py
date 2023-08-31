import board

game_over = False
turn_count = 0

def player_turn():
      global game_over
      global turn_count
      if turn_count % 2 == 0:
            move = input("X move. Place your move: ")
            if move == 'q': 
                  game_over = True
            else: 
                  board.placement[int(move)] = 'X'
                  turn_count += 1
                  board.display()
      else:
            move = input("O move. Place your move: ")
            if move == 'q': 
                  game_over = True
            else: 
                  board.placement[int(move)] = 'O'
                  turn_count += 1
                  board.display()

board.display()
while not game_over:
      player_turn()
      print(turn_count)



