import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, root):
        self.size = 3           
        self.win_length = 3     
        self.root = root
        self.root.title("Tic-Tac-Toe () - You: X | Computer: O")
        self.board = [' ' for _ in range(self.size * self.size)]
        self.buttons = []
        self.player = 'X'
        self.computer = 'O'
        self.create_board()

    def create_board(self):
        for i in range(self.size * self.size):
            button = tk.Button(self.root, text=' ', font='Helvetica 16', height=2, width=4,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i // self.size, column=i % self.size)
            self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] == ' ':
            self.make_move(index, self.player)
            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_board()
                return
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
                return
            self.root.after(300, self.computer_move)

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index]['text'] = player
        self.buttons[index]['state'] = 'disabled'

    def is_draw(self):
        return ' ' not in self.board

    def check_winner(self, player):
        for row in range(self.size):
            for col in range(self.size):
                if self.check_direction(row, col, 1, 0, player):  
                    return True
                if self.check_direction(row, col, 0, 1, player):  
                if self.check_direction(row, col, 1, 1, player):  
                    return True
                if self.check_direction(row, col, 1, -1, player): 
                    return True
        return False

    def check_direction(self, row, col, d_row, d_col, player):
        count = 0
        for i in range(self.win_length):
            r = row + d_row * i
            c = col + d_col * i
            if 0 <= r < self.size and 0 <= c < self.size:
                if self.board[r * self.size + c] == player:
                    count += 1
                else:
                    break
            else:
                break
        return count == self.win_length

    def computer_move(self):
        best_score = -math.inf
        best_move = None
        for move in self.available_moves():
            self.board[move] = self.computer
            score = self.minimax(0, False, -math.inf, math.inf)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        self.make_move(best_move, self.computer)

        if self.check_winner(self.computer):
            messagebox.showinfo("Game Over", "Computer wins!")
            self.reset_board()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.check_winner(self.computer):
            return 10 - depth
        elif self.check_winner(self.player):
            return depth - 10
        elif self.is_draw() or depth >= 2:  
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for move in self.available_moves():
                self.board[move] = self.computer
                eval = self.minimax(depth + 1, False, alpha, beta)
                self.board[move] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.available_moves():
                self.board[move] = self.player
                eval = self.minimax(depth + 1, True, alpha, beta)
                self.board[move] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def reset_board(self):
        self.board = [' ' for _ in range(self.size * self.size)]
        for btn in self.buttons:
            btn.config(text=' ', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()



