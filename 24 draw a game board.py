# function for game board
def game_board():
    r = int(input("Please enter the number of rows: "))
    c = int(input("Please enter the number of columns: "))

    # define rows
    def row():
        print("--- " * r)

    # define columns
    def column():
        print("| " * c)

    # Loop to make game board
    for x in range(r):
        row()
        column()

    row()


game_board()
