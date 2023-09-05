# each placement on the board has a position & symbol
placement = {1: '1',
             2: '2',
             3: '3',
             4: '4',
             5: '5',
             6: '6',
             7: '7',
             8: '8',
             9: '9',}

def display():
    # print board - display using placement dictionary
    print(f'{placement[1]} | {placement[2]} | {placement[3]} \n'
          '--------- \n'
          f'{placement[4]} | {placement[5]} | {placement[6]} \n'
          '--------- \n'
          f'{placement[7]} | {placement[8]} | {placement[9]} \n')
    
def winner():
      # check if the 3 horizontal plays are the same
      if (placement[1] == placement[2] == placement[3]) \
        or (placement[4] == placement[5] == placement[6]) \
        or (placement[7] == placement[8] == placement[9]):
            return True
      # check if the 3 vertical plays are the same
      elif (placement[1] == placement[4] == placement[7]) \
         or (placement[2] == placement[5] == placement[8]) \
         or (placement[3] == placement[6] == placement[9]):
            return True
      # check if the 2 diagonal plays are the same
      elif (placement[1] == placement[5] == placement[9]) \
         or (placement[7] == placement[5] == placement[3]):
            return True
