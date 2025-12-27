import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")


current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]




def check_winners():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    
    return False

def check_tie():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def on_click(row, col):
    global current_player

    if board[row][col] != "":
        return
    
    board[row][col] = current_player
    buttons[row][col].config(text=current_player)

    if check_winners():
        messagebox.showinfo("Game over", f"Player {current_player} wins!")
        reset_game() #Code later
        return

    current_player = "O" if current_player == "X" else "X"


def reset_game():
    global current_player
    current_player = "X"

    for r in range(3):
        for c in range(3):
            board[r][c] = ""
            buttons[r][c].config(text="")

def closing():
    if messagebox.askyesno(title='Quit?', message="You want to close Tic-Tac-Toe?"):
        root.destroy()

for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(
            root,
            text="",
            font=("Arial", 14),
            width=5,height=2,
            command=lambda r=r, c=c: on_click(r, c)
        )
        buttons[r][c].grid(row=r, column=c)
        buttons[r][c].grid(row=r, column=c)

root.protocol("WM_DELETE_WINDOW", closing)
reset_btn = tk.Button(root, text="Reset", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="we")

root.mainloop()