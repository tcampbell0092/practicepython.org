# ask user to play game or quit

terminate = input('Lets play Rock, Paper Scissors! Press any button to continue or Quit to exit: ')
while terminate != 'Quit':
    # user input for choosing rock, paper or scissors
    player1 = input('Player 1, Rock, Paper, or Scissors?: ')
    player2 = input('Player 2, Rock, Paper, or Scissors?: ')

    # conditional statements to compare results
    if player1 == 'Rock' and player2 == 'Paper':
        print('Player 2 Wins!')

    if player1 == 'Paper' and player2 == 'Rock':
        print('Player 1 Wins!')

    if player1 == 'Scissors' and player2 == 'Paper':
        print('Player 1 Wins!')

    if player1 == 'Paper' and player2 == 'Scissors':
        print('Player 2 Wins!')

    if player1 == 'Rock' and player2 == 'Scissors':
        print('Player 1 Wins!')

    if player1 == 'Scissors' and player2 == 'Rock':
        print('Player 2 Wins!')

    # user input to continue or quit game
    choice = input('Play again? Press any button to Continue, No to Quit: ')
    if choice == 'No':
        print('Thanks for playing!')
        break




