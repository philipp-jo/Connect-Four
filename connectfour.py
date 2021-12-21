import random


class Player:
    
    def __init__(self, num):
        self.name = input('Player ' + str(num) + ', please enter your name: ')
        self.symb = input(self.name + ', please choose your symbol: ')

class ConnectFour:

    def __init__(self):
        self.board = []
    
    def setup_board(self):
        for i in range(6):
            row = ['-','-','-','-','-','-','-']
            self.board.append(row)

    def display_board(self):
        for row in self.board:
            for item in row:
                print(item, end='  ')
            print()

    def starting_player(self):
        return random.randint(0,1)

    def fill_spot(self, symbol, row, column):
        self.board[row][column-1] = symbol

    # player enters column; search for lowest empty row in that column
    def get_empty_row(self, column):
        n = len(self.board)
        row_count = -1
        for i in range(n): # goes through each row in the board
            row_count += 1 # increase row_count for each row
            if self.board[i][column-1] != '-':
                row_count -= 1
                return row_count
            elif self.board[n-1][column-1] == '-': # returns lowest row if column is empty
                return n-1
    
    def check_if_won(self, symbol):
        win = None
        reversed_board = list(reversed(self.board))
        n = len(self.board)

        # checking rows
        for i in range(n):
            row = self.board[i]
            for j in range(4):
                if row[j] == symbol and row[j+1] == symbol and row[j+2] == symbol and row[j+3] == symbol:
                    win = True
                    break
                else:
                    win = False
            if win:
                return win
        
        # checking columns
        for i in range(3):
            for j in range(7):
                if self.board[i][j] == symbol and self.board[i+1][j] == symbol and self.board[i+2][j] == symbol and self.board[i+3][j] == symbol:
                    win = True
                    break
                else:
                    win = False
            if win:
                return win
        
        # checking diagonals
        for i in range(3):
            for j in range(n):
                if self.board[i][j] == symbol and self.board[i+1][j+1] == symbol and self.board[i+2][j+2] == symbol and self.board[i+3][j+3] == symbol:
                    win = True
                    break
                elif reversed_board[i][j] == symbol and reversed_board[i+1][j+1] == symbol and reversed_board[i+2][j+2] == symbol and reversed_board[i+3][j+3] == symbol:
                    win = True
                    break
                else:
                    win = False
            if win:
                return win 
        
    
    def is_game_draw(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def game_start(self):
        message = '''
         # # #   ####   #     #  #     #  # # #   # # #  # # # # #       #   #
        #       #    #  # #   #  # #   #  #      #           #           #   #
        #       #    #  #  #  #  #  #  #  # # #  #           #     ####  # # #
        #       #    #  #   # #  #   # #  #      #           #               #
         # # #   ####   #     #  #     #  # # #   # # #      #               #
        '''
        print(message)
        print('############################################################################################')
        print('#   Welcome to Connect-4. This game is created and maintained by GitHub user philipp-jo.   #')
        print('############################################################################################')

        #init players
        player1 = Player(1)
        player2 = Player(2)

        # init gameboard
        self.setup_board()

        # determine starting player
        player_symb = player1.symb if self.starting_player == 1 else player2.symb
        player_name = player1.name if self.starting_player == 1 else player2.name

        while True:
            print('{player}\'s turn.'.format(player=player_name))
            self.display_board()

        # current player should choose column to place their symbol in
            while True:
                col = int(input(player_name + ", please enter a column number: "))
                if col-1 in range(7):
                    if self.get_empty_row(col) in range(6): # checks if a row in column is empty
                        break
                
        # symbol is placed in lowest row possible
            row = self.get_empty_row(col)
            self.fill_spot(player_symb, row, col)
        
        # check if game is won
            if self.check_if_won(player_symb):
                print(player_name + ' has won the game!')
                break
        
        # check if game is draw
            if self.is_game_draw():
                print('It\'s a draw!')
                break
        
        # switch player if neither won or draw
            if player_name == player1.name and player_symb == player1.symb:
                player_name = player2.name
                player_symb = player2.symb
            else:
                player_name = player1.name
                player_symb = player1.symb
        print()
        self.display_board()


game = ConnectFour()
game.game_start()