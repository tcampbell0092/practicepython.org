# define game board
board = [[1, 0, 1],
         [2, 0, 1],
         [2, 0, 2]]

# define game dictionary
game_dict = {}


# define game resolution
def tic_tac():
    for i in range(3):
        game_dict[i] = board[i]
    column = 0
    no_winner = 0
    while column < 3:
        row = 0
        column_list = []
        while row < 3:
            column_list.append(game_dict[row][column])
            row += 1
        # test for winner vertically
        if column_list[0] == column_list[1] == column_list[2] and 0 not in column_list:
            print("Player #%d wins vertically." % column_list[0])
        else:
            no_winner += 1
        column += 1
    for n in range(3):
        # test for winner horizontally
        if game_dict[n][0] == game_dict[1] == game_dict[2] and 0 not in game_dict:
            print("Player #%d wins horizontally." % game_dict[n][n])
        else:
            no_winner += 1
    if no_winner == 6:
        print("There is no winner.")


tic_tac()
