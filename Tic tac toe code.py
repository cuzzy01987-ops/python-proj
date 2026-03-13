# tic tac toe game in python
import random

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
        
class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [' ' for _ in range(20)]
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
    def winner(self, square, marker):
        row_ind = square // 3
        if all([spot == marker for spot in self.board[row_ind*3:(row_ind+1)*3]]):
            return True
        col_ind = square % 3
        if all([self.board[col_ind+i*3] == marker for i in range(3)]):
            return True
        if square % 2 == 0:
            if all([self.board[i] == marker for i in [0, 4, 8, ]]):
                return True
            if all([self.board[i] == marker for i in [2, 4, 6, 8, ]]):
                return True
        return False
    
    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
        
    def play_game(self):
        print(f"{self.current_player.name} starts first with marker '{self.current_player.marker}'")
        while ' ' in self.board:
            self.print_board()
            square = None
            while square not in self.available_moves():
                try:
                    square = int(input(f"{self.current_player.name} ({self.current_player.marker}), choose your move (0-20): "))
                    if square not in self.available_moves():
                        print("This square is already occupied or out of range. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 20.")
            self.make_move(square, self.current_player.marker)
            if self.current_winner:
                self.print_board()
                print(f"{self.current_player.name} wins!")
                return
            self.switch_player()
        self.print_board()
        print("It's a tie!")
        
if __name__ == '__main__':
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    tictactoe = TicTacToe(player1, player2)
    tictactoe.play_game()
    
    
    