class Connect_Four():

    COL_COUNT = 7
    ROW_COUNT = 6

    def __init__(self):
        self.board = [[' ' for i in range(Connect_Four.COL_COUNT)] for j in range(Connect_Four.ROW_COUNT)]


    def print_board(self):
        result = ''
        for i in self.board:
            result += '-' * 15 + '\n'
            for j in i:
                result += f'|{j}'
            result += '|\n'
        result += '-' * 15
        print(result)



    def drop(self, col, team: str):
        if col:
            if col.isdigit():
                col = int(col)
                if col < 7 and col > -1 or col == None:
                    col -= 1
                    if self.board[0][col] == ' ':
                        for i in range(5, -1, -1):
                            if self.board[i][col] == ' ':
                                self.board[i][col] = team
                                break
                    else:
                        print('That column is full dill weed.  Look much?  You\'ve lost your turn')
                else:
                    print('1... to... 7... dumbass...  You lose your turn')
            else:
                print('NUMBERS (WO)MAN!  I NEED NUMBERS!  Lose a turn.')
        else:
            print('... You have to enter something you troglodite.  Lose a turn')

    def check(self, team: str):
        # check horizontal wins
        for i in range(Connect_Four.COL_COUNT - 3):
            for j in range(Connect_Four.ROW_COUNT):
                if self.board[j][i] == team and self.board[j][i + 1] == team and self.board[j][i + 2] == team and \
                        self.board[j][i + 3] == team:
                    return True

        # check for vertical wins
        for c in range(Connect_Four.COL_COUNT):
            for r in range(Connect_Four.ROW_COUNT - 3):
                if self.board[r][c] == team and self.board[r + 1][c] == team and self.board[r + 2][c] == team and \
                        self.board[r + 3][c] == team:
                    return True

        # check for diagonal right wins (works)
        for c in range(Connect_Four.COL_COUNT-3):
            for r in range(Connect_Four.ROW_COUNT-3):
                if self.board[r][c] == team and self.board[r+1][c+1] == team and self.board[r+2][c+2] == team and self.board[r+3][c+3] == team:
                    return True

        # check for diagonal left wins (works)
        for c in range(Connect_Four.COL_COUNT-4, Connect_Four.COL_COUNT):
            for r in range(Connect_Four.ROW_COUNT-3):
                if self.board[r][c] == team and self.board[r+1][c-1] == team and self.board[r+2][c-2] == team and self.board[r+3][c-3] == team:
                    return True

    def check_tie(self):
        '''
        Check for a tie on the board, this occurs if all spaces have been filled and no player
        has completed a 'connect 4'.
        Returns: Boolean, True for tie, False if no tie
        '''
        for i in self.board:
            for j in i:
                if j == ' ':
                    return False
        return True

if __name__ == '__main__':
    board = Connect_Four()
    board.print_board()

    team1, team2 = '', ''

    while len(team1) != 1:
        team1 = input('Enter a character to use as your token player 1: ')

    while len(team2) != 1 and team1 != team2:
        team2 = input('Enter a character to use as your token player 2: ')
        if team2 == team1:
            print('Please choose a token different from player 1...  How ya gonna tell the difference in teams?  Dummy.')


    while not board.check(team1) and not board.check(team2):
        col = input(f'Player 1 ({team1}) insert piece in col (1-7): ')
        board.drop(col, team1)
        board.print_board()

        if board.check(team1):
            print(f'PLAYER 1 ({team1}) WINS!')
            quit()

        if board.check_tie():
            print('GAME TIED!  YOU BOTH LOSE!')
            quit()

        col = input(f'Player 2 ({team2}) insert piece in col (1-7): ')
        board.drop(col, team2)
        board.print_board()

        if board.check(team2):
            print(f'PLAYER 2 ({team2}) WINS!')
            quit()

        if board.check_tie():
            print('GAME TIED!  YOU BOTH LOSE!')
            quit()