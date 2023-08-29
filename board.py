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
