from board import display, winner, placement

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
                  placement[int(move)] = 'X'
                  turn_count += 1
                  display()
      else:
            move = input("O move. Place your move: ")
            if move == 'q': 
                  game_over = True
            else: 
                  placement[int(move)] = 'O'
                  turn_count += 1
                  display()

display()
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
      
