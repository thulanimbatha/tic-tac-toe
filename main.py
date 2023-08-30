import board

game_over = False

board.display()
while not game_over:
      turn = input("X turn. Place your move")
      if turn == 'q': game_over = True
      else: 
            board.placement[int(turn)] = 'X'
            board.display()



