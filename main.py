import board

game_over = False
turn_count = 0
X_moves = []
O_moves = []
winning_combos = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2], #rows
                  [4,5,6], [4,6,5], [5,4,6], [5,6,4], [6,4,5], [6,5,4],
                  [7,8,9], [7,9,8], [8,7,9], [8,9,7], [9,7,8], [9,8,7],
                  [1,4,7], [1,7,4], [4,1,7], [4,7,1], [7,1,4], [7,4,1], #columns
                  [2,5,8], [2,8,5], [5,2,8], [5,8,2], [8,2,5], [8,5,2],
                  [3,6,9], [3,9,6], [6,3,9], [6,9,3], [9,3,6], [9,6,3],
                  [1,5,9], [1,9,5], [5,1,9], [5,9,1], [9,1,5], [9,5,1], #diagonal
                  [3,5,7], [3,7,5], [5,3,7], [5,7,3], [7,3,5], [7,5,3]]

def player_turn():
      global game_over
      global turn_count
      if turn_count % 2 == 0:
            move = input("X move. Place your move: ")
            if move == 'q': 
                  game_over = True
            else: 
                  X_moves.append(int(move))
                  board.placement[int(move)] = 'X'
                  turn_count += 1
                  board.display()
      else:
            move = input("O move. Place your move: ")
            if move == 'q': 
                  game_over = True
            else: 
                  O_moves.append(int(move))
                  board.placement[int(move)] = 'O'
                  turn_count += 1
                  board.display()

board.display()
while not game_over:
      player_turn()
      print(turn_count)
      if X_moves in winning_combos:
            print("Winner")
            game_over = True
      elif O_moves in winning_combos:
            print("Winner")
            game_over = True





