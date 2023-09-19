from board import display, winner, placement
import os

game_over = False
turn_count = 0

'''DETERMINE WHICH PLAYER HAS MOVE NEXT'''
def player_symbol():
      global turn_count
      # check turn count - determine play turn
      # if turn count mod 2 is 0 - X turn
      if turn_count % 2 == 0 or turn_count % 2 == 2:
            return 'X'            
      # else if turn count mod 2 is 1 - O turn
      else:
            return 'O'

'''CHANGING DISPLAY BASED ON WHICH PLAYER TURN''' 
def change_display(chosen_move):
      global game_over
      global turn_count

      if player_symbol() == 'X':
            # check to see if spot is already marked with 'X' or 'O'
            if placement[int(chosen_move)] == 'X' or placement[int(chosen_move)] == 'O':
                  print('Spot already taken! Choose an available spot!'.upper())
            else:
            # if not, change display with new marking
                  placement[int(chosen_move)] = 'X'
                  turn_count += 1

      elif player_symbol() == 'O':
            # check to see if spot is already marked with 'X' or 'O'
            if placement[int(chosen_move)] == 'O' or placement[int(chosen_move)] == 'X':
                  print('Spot already taken! Choose an available spot!'.upper())
            else:
            # if not, change display with new marking
                  placement[int(chosen_move)] = 'O'
                  turn_count += 1

'''CLEAR THE SCREEN'''
def clear_screen():
      os.system('cls' if os.name == 'nt' else 'clear')

'''DETERMINE TYPE OF USER INPUT'''
def player_move():
      global game_over

      display()
      move = input(f"{player_symbol()} move. Place your move. ('q' to quit): ")

      # 'q' to quit game
      if move == 'q':
            game_over = True
            print('Goodbye!')
      # check is digit is between 1 and 9
      elif move.isdigit() and 0 < int(move) and int(move) < 10:
            clear_screen()
            change_display(move)
      # everything else, invalid
      else:
            clear_screen() 
            print('Invalid selection! Please select "q" to quit, or number 1-9') 
                 
'''START'''
while not game_over:
      # game has maximum 9 moves/turns
      if turn_count == 9:
            print('DRAW!')
            game_over = True
      # if there is no winner yet, continue playing
      elif not winner():
            player_move()
      # winner found
      else:
            display()
            turn_count -= 1
            print(f'{player_symbol()} WINS!')
            game_over = True
      
