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

def winner():
      # check if the 3 horizontal plays are the same
      if (board.placement[1] == board.placement[2] == board.placement[3]) \
        or (board.placement[4] == board.placement[5] == board.placement[6]) \
        or (board.placement[7] == board.placement[8] == board.placement[9]):
            return True
      # check if the 3 vertical plays are the same
      elif (board.placement[1] == board.placement[4] == board.placement[7]) \
         or (board.placement[2] == board.placement[5] == board.placement[8]) \
         or (board.placement[3] == board.placement[6] == board.placement[9]):
            return True
      # check if the 2 diagonal plays are the same
      elif (board.placement[1] == board.placement[5] == board.placement[9]) \
         or (board.placement[7] == board.placement[5] == board.placement[3]):
            return True

board.display()
while not game_over:
      if turn_count == 9:
            print('DRAW!')
            game_over = True
      elif not winner():
            player_turn()
            print(turn_count)
      else:
            print('WINNER!')
            game_over = True
      
