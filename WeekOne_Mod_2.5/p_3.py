playerOne = input('Player 1: ')
playerTwo = input('Player 2: ')

if playerOne=='rock':
    if playerTwo=='paper':
        print('Player 2 is winner')
    elif playerTwo=='scissors':
        print('Player 1 is winner')
elif playerOne=='scissors':
    if playerTwo=='rock':
        print('Player 2 is winner')
    elif playerTwo=='paper':
        print('Player 1 is winner')
elif playerOne=='paper':
    if playerTwo=='scissors':
        print('Player 2 is winner')
    elif playerTwo=='rock':
        print('Player 1 is winner')