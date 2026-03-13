import random 

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
        
class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1 if random.choice([True, False]) else player2
        
        
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print()
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, marker):
        if self.board[square] == ' ':
            self.board[square] = marker
            if self.winner(square, marker):
                self.current_winner = marker
            return True
        return False
    