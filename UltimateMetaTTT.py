# ----------------------------------------------------
# Assignment 2: Tic Tac Toe classes
#
# Author: Dhiraj Meenavilli
# References: Lab 3
# ----------------------------------------------------

class NumTicTacToe: # This code was pulled from the lab 3 code
    def __init__(self):
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3  # number of columns and rows of board

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.board.append(row)

    def drawBoard(self):

        board = '   0   1   2 \n0  {} | {} | {}\n  ----------- \n1  {} | {} | {}\n  ----------- \n2  {} | {} | {}\n  ----------- \n'
        board = board.format(self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],self.board[2][2])
        print(board)

    def squareIsEmpty(self, row, col):

        if self.board[row][col] > 0:
            return False

        else:
            return True

    def update(self, row, col, num):

        if self.squareIsEmpty(row,col):
            self.board[row][col] = num
            return True

        else:
            return False

    def boardFull(self):

        filled = 0
        for u in range(len(self.board)):
            for b in range(len(self.board)):
                if not self.squareIsEmpty(u,b):
                    filled += 1

        if filled == 9:
            return True
        else:
            return False

    def isWinner(self):

        decided = 0
        for i in range(3):
            if self.board[0][i] + self.board[1][i] + self.board[2][i] == 15:
                decided += 1
                return True

        for i in range(3):
            if self.board[i][0] + self.board[i][1] + self.board[i][2] == 15:
                decided += 1
                return True

        if self.board[0][0] + self.board[1][1] + self.board[2][2] == 15:
            decided += 1
            return True

        if self.board[0][2] + self.board[1][1] + self.board[2][0] == 15:
            decided += 1
            return True

        if decided == 0:
            return False

    def isNum(self):
        return True


class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3  # number of columns and rows of board

        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.board.append(row)

    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row
        indices shown.
        Inputs: none
        Returns: None
        '''

        board = '   0   1   2 \n0  {} | {} | {}\n  ----------- \n1  {} | {} | {}\n  ----------- \n2  {} | {} | {}\n  ----------- \n'
        board = board.format(self.board[0][0], self.board[0][1], self.board[0][2], self.board[1][0], self.board[1][1],self.board[1][2], self.board[2][0], self.board[2][1], self.board[2][2])
        print(board)

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == "X" or self.board[row][col] == "O":
            return False

        else:
            return True

    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column,
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col):
            self.board[row][col] = mark
            return True

        else:
            return False

    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        filled = 0
        for u in range(len(self.board)):
            for b in range(len(self.board)):
                if not self.squareIsEmpty(u, b):
                    filled += 1

        if filled == 9:
            return True
        else:
            return False

    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move;
                 False otherwise
        '''
        decided = 0
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == 'X':
                    print("Player 1 has won")
                    decided += 1
                    return True
                if self.board[0][i] == "O":
                    print("Player 2 has won")
                    decided += 1
                    return True
                else:
                    return False

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == 'X':
                    print("Player 1 has won")
                    decided += 1
                    return True
                if self.board[i][1] == "O":
                    print("Player 2 has won")
                    decided += 1
                    return True
                else:
                    return False

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                print("Player 1 has won")
                decided += 1
                return True
            if self.board[1][1] == "O":
                print("Player 2 has won")
                decided += 1
                return True
            else:
                return False

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == 'X':
                print("Player 1 has won")
                decided += 1
                return True
            if self.board[1][1] == "O":
                print("Player 2 has won")
                decided += 1
                return True
            else:
                return False

        if decided == 0:
            return False

    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        return False


class MetaTicTacToe:
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a
        configuration file.
        Inputs:
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''

        try:
            cf = open(configFile,'r')
            cf = cf.read()
            cf = list(cf)
            for i in range(6):
                cf.remove(" ")
            for i in range(2):
                cf.remove("\n")
            self.config = cf
        except FileNotFoundError:
            print("This file cannot be found.")
        except:
            print("Unknown error occured.")

        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3  # number of columns and rows of board

        pos = 0 # This acts as a pointer to help tell the program which piece of the config file goes where
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(self.config[pos])
                pos += 1
            self.board.append(row)

    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row
        indices shown.
        Inputs: none
        Returns: None
        '''
        board = '   0   1   2 \n0  {} | {} | {}\n  ----------- \n1  {} | {} | {}\n  ----------- \n2  {} | {} | {}\n  ----------- \n'
        board = board.format(self.board[0][0], self.board[0][1], self.board[0][2], self.board[1][0], self.board[1][1],
                             self.board[1][2], self.board[2][0], self.board[2][1], self.board[2][2])
        print(board)

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == "D" or self.board[row][col] == "X" or self.board[row][col] == "O":
            return False
        else:
            return True

    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column,
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col):
            self.board[row][col] = result
            return True

        else:
            return False


    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''

        filled = 0
        for u in range(len(self.board)):
            for b in range(len(self.board)):
                if not self.squareIsEmpty(u, b):
                    filled += 1

        if filled == 9:
            return True
        else:
            return False

    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move;
                 False otherwise
        '''
        decided = 0
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == 'X':
                    print("Player 1 has won")
                    decided += 1
                    return True
                if self.board[0][i] == "O":
                    print("Player 2 has won")
                    decided += 1
                    return True
                if self.board[0][i] == "D":
                    print("Current Player has won")
                    decided += 1
                    return True
                else:
                    return False

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == 'X':
                    print("Player 1 has won")
                    decided += 1
                    return True
                if self.board[i][1] == "O":
                    print("Player 2 has won")
                    decided += 1
                    return True
                if self.board[i][2] == "D":
                    print("Current Player has won")
                    decided += 1
                    return True
                else:
                    return False

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                print("Player 1 has won")
                decided += 1
                return True
            if self.board[1][1] == "O":
                print("Player 2 has won")
                decided += 1
                return True
            if self.board[2][2] == "D":
                print("Current Player has won")
                decided += 1
                return True
            else:
                return False

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == 'X':
                print("Player 1 has won")
                decided += 1
                return True
            if self.board[1][1] == "O":
                print("Player 2 has won")
                decided += 1
                return True
            if self.board[2][0] == "D":
                print("Current Player has won")
                decided += 1
                return True
            else:
                return False

        if decided == 0:
            return False

    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played;
                 None if local board has already been played
        '''
        if self.squareIsEmpty(row,col):
            if self.board[row][col] == 'c':
                board = ClassicTicTacToe()
            elif self.board[row][col] == "n":
                board = NumTicTacToe()
            return board
        elif not self.squareIsEmpty(row,col):
            return None

def rules(board,player):
    marks = ["X","O"]

    if board.isNum():
        valid = False
        if player % 2 == 0:
            numDescription = 'even'
            lowerRange = 2
            upperRange = 8
        else:
            numDescription = 'odd'
            lowerRange = 1
            upperRange = 9
        prompt = 'Player {}, please enter an {} number ({}-{}): '
        prompt = prompt.format(player, numDescription, lowerRange, upperRange)
        while not valid:
            val = int(input(prompt))

            if player % 2 != entry % 2 or entry > upperRange or entry < lowerRange:
                valid = False

            else:
                valid = True

        return val

    if not board.isNum():
        val = marks[player % 2]
        return val

def main():
    ### ----------------------------------------------------- Classic and Number Tic Tac Toe Board Tests ------------------------------------------------- ###
    """
    # Test 1 - Do the boards intitalize, look how they should, and return the correct boolean for wether they are a number board or not
    nb = NumTicTacToe()
    cb = ClassicTicTacToe()
    nb.drawBoard()
    cb.drawBoard()
    print(nb.isNum(),cb.isNum(),"\n")
    """
    """
    # Test 2 Do the boards square empty and is winner methods work correctly
    for i in range(3):
        for j in range(3):
            print("row",i,"col",j,"for the numerical board is empty:",nb.squareIsEmpty(i,j))
            print("row",i,"col",j,"for the classic board is empty:",cb.squareIsEmpty(i,j))

    print("\nThere is a Numeric winner:",nb.isWinner()) # A mini test to see that true isn't being returned when the player hasn't actually won
    print("There is a Classic winner:", cb.isWinner())
    """
    """
    #This is a check to see if the horizontal win can be achieved

    nb.update(0,0,3)
    nb.update(0,1,5)
    nb.update(0,2,7)

    cb.update(0,0,"X")
    cb.update(0,1,"X")
    cb.update(0,2,"X")
    """

    """
    #This a check to see if the vertical win can be achieved
    nb.update(0,0,3)
    nb.update(1,0,5)
    nb.update(2,0,7)

    cb.update(0, 0, "X")
    cb.update(1, 0, "X")
    cb.update(2, 0, "X")
    """

    """
    # This tests the top left to bottom right diagonal win
    nb.update(0, 0, 3)
    nb.update(1, 1, 5)
    nb.update(2, 2, 7)

    cb.update(0, 0, "X")
    cb.update(1, 1, "X")
    cb.update(2, 2, "X")
    """

    """
    # This tests the top right to bottom left diagonal win
    nb.update(2, 0, 3)
    nb.update(1, 1, 5)
    nb.update(0, 2, 7)

    cb.update(2, 0, "X")
    cb.update(1, 1, "X")
    cb.update(0, 2, "X")


    nb.drawBoard() # These are once again being tested to see if they work appropriatley
    cb.drawBoard()

    print("\nThere is a Numeric winner:",nb.isWinner())
    print("There is a Classic winner:", cb.isWinner(),"\n")
    """
    """
    # Test 3 - Checks to see if the board is full and if the squareIsEmpty method isn't incorrectly returning True
    for i in range(3):
        for j in range(3):
            nb.update(i,j,2)
            cb.update(i,j,"X")
            print("Row",i,"col",j,"is empty: ",nb.squareIsEmpty(i,j))
            print("Row",i,"col",j,"is empty: ",cb.squareIsEmpty(i,j))

    print("\nNumeric Board is full: ",nb.boardFull(),"\nClassic Board is full: ",cb.boardFull())
    """
    ### ---------------------------------------- Meta Tic Tac Toe Tests --------------------------------------------- ###
    """
    # Test 1 - A check to see if the board initalizes correctly
    configFile = 'MetaTTTconfig.txt'
    mtt = MetaTicTacToe(configFile)
    mtt.drawBoard()
    """
    """
    # Test 2 - A check to see that the getLocalBoard method works and that the instance generated is the correct type and can be interacted with correctly.
    board = mtt.getLocalBoard(0,0)
    board.drawBoard()
    board.update(0,0,"3")
    board.drawBoard()
    print(type(board))

    board = mtt.getLocalBoard(2,0)
    print(type(board),"\n")
    """
    """
    # Test 3 - A check on the isWinner drawBoard and update functions
    for i in range(3):
        for j in range(3):
            print("Row",i,"col",j,"is empty: ",mtt.squareIsEmpty(i,j))

    print("The Meta Tic Tac Toe board has a winner:", mtt.isWinner())
    mtt.drawBoard()

    for i in range(3):
        mtt.update(0,i,"X")

    mtt.drawBoard()

    print("The Meta Tic Tac Toe board is full: ", mtt.boardFull())

    print("The Meta Tic Tac Toe board has a winner: ", mtt.isWinner())

    for i in range(3):
        for j in range(3):
            mtt.update(i,j,"X")

    mtt.drawBoard()

    print("The Meta Tic Tac Toe board is full: ", mtt.boardFull())

    mtt.update(0,0,"O") # A check to make sure the board doesn't fill in if the square is not empty
    mtt.drawBoard()
    print("The board is full: ", mtt.boardFull())
    """

    ### ---------------------------------------------------- Code Starts Here -------------------------------------- ###

    game  = True
    marks = ["X","O"]
    players = [" Player 1", " Player 2"]
    configFile = 'MetaTTTconfig.txt'
    mtt = MetaTicTacToe(configFile)
    metaTurn = 0

    while game:
        mtt.drawBoard()
        metaValid = False

        while not metaValid:
            try:
                metaRow = int(input('What is the row of the cell you would like to access'+ players[metaTurn%2] + "\n"))
                metaCol = int(input('What is the column of the cell you would like to access'+players[metaTurn%2] + "\n"))
                if mtt.squareIsEmpty(metaRow,metaCol):
                    board = mtt.getLocalBoard(metaRow,metaCol)
                    metaValid = True
            except:
                print("Please enter an appropriate input.\n")
        ongoing = True
        board.drawBoard()
        turn = 0
        while ongoing:
            valid = False

            while not valid:

                correct = False

                try:

                    while not correct:
                        row = int(input('What is the row of the cell you would like to access\n'))
                        col = int(input('What is the column of the cell you would like to access\n'))
                        if board.squareIsEmpty(row,col):
                            val = rules(board,turn)
                            correct = True
                        else:
                            print("That square is not empty please choose another.")

                    board.update(row,col,val)
                    valid = True
                except:
                    print("Please enter an appropriate input.\n")

            board.drawBoard()

            if board.isWinner():
                mtt.update(metaRow, metaCol, marks[turn % 2])
                ongoing = False

            if board.boardFull():
                mtt.update(metaRow, metaCol, "D")
                ongoing = False

            turn += 1
        metaTurn += 1
        if mtt.isWinner():
            game = False


if __name__ == "__main__":
    main()
