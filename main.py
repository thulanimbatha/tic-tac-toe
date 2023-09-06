from board import display, winner, placement

game_over = False
turn_count = 0

def player_symbol():
      global turn_count
      # check turn count - determine play turn
      # if turn count mod 2 is 0 - X turn
      if turn_count % 2 == 0 or turn_count % 2 == 2:
            return 'X'            
      # else if turn count mod 2 is 1 - O turn
      else:
            return 'O'
      
def change_display(chosen_move):
      global game_over
      global turn_count

      if player_symbol() == 'X':
            placement[int(chosen_move)] = 'X'

      elif player_symbol() == 'O':
            placement[int(chosen_move)] = 'O'
      
      turn_count += 1

def player_move():
      global game_over

      display()
      # change board display based on X or O placement
      move = input(f"{player_symbol()} move. Place your move. ('q' to quit): ")
      if move == 'q':
            game_over = True
      elif move.isalpha() or move.isspace():
            print('Invalid selection! Please select "q" to quit, or number 1-9')
      elif move.isalnum():
            if move.isdigit() and 0 < int(move) and int(move) < 10:
                  change_display(move)
            else: 
                  print('Invalid selection! Please select "q" to quit, or number 1-9')
      

# start gameplay
while not game_over:
      if turn_count == 9:
            print('DRAW!')
            game_over = True
      elif not winner():
            player_move()
      else:
            display()
            turn_count -= 1
            print(f'{player_symbol()} WINS!')
            game_over = True
      
