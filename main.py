from tkinter import *
from tkinter import (
    messagebox,
    ttk,
)

current_player = "X"
game_over = False


def check_win(player):
    for r in range(3):
        if (
            buttons[r][0]["text"] == player
            and buttons[r][1]["text"] == player
            and buttons[r][2]["text"] == player
        ):
            return True
    for c in range(3):
        if (
            buttons[0][c]["text"] == player
            and buttons[1][c]["text"] == player
            and buttons[2][c]["text"] == player
        ):
            return True
    if (
        buttons[0][0]["text"] == player
        and buttons[1][1]["text"] == player
        and buttons[2][2]["text"] == player
    ):
        return True
    if (
        buttons[0][2]["text"] == player
        and buttons[1][1]["text"] == player
        and buttons[2][0]["text"] == player
    ):
        return True
    return False


def check_draw():
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"] == "":
                return False
    return True


def disable_all_buttons():
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(state="disabled")


def on_square_click(row, col):
    global current_player, game_over

    if buttons[row][col]["text"] != "" or game_over:
        return

    buttons[row][col].config(text=current_player, state="disabled")

    if check_win(current_player):
        messagebox.showinfo("Tkic Tac Toer", f"{current_player} wins!")
        game_over = True
        disable_all_buttons()
    elif check_draw():
        messagebox.showinfo("Tkic Tac Toer", "It's a draw!")
        game_over = True
    else:
        current_player = "O" if current_player == "X" else "X"


def start_new_game():
    global current_player, game_over
    current_player = "X"
    game_over = False
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", state="normal")


root = Tk()
root.title("Tkic Tac Toer")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(bg="#000000")

style = ttk.Style()
style.configure("Main.TFrame", background="#000000")
style.configure("Game.TButton", font=("", 24, "bold"), padding=35)

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=0)

board_frame = ttk.Frame(mainframe, padding="5 5 5 5", style="Main.TFrame")
board_frame.grid(column=0, row=0, sticky=(N, W, E, S))

for i in range(3):
    board_frame.columnconfigure(i, weight=1, minsize=60)
    board_frame.rowconfigure(i, weight=1, minsize=60)

buttons = [[None for _ in range(3)] for _ in range(3)]

for r in range(3):
    for c in range(3):
        btn = ttk.Button(
            board_frame,
            text="",
            style="Game.TButton",
            command=lambda row=r, col=c: on_square_click(row, col),
        )
        btn.grid(row=r, column=c, sticky=(N, S, E, W), padx=2, pady=2)
        buttons[r][c] = btn

new_game_button = ttk.Button(mainframe, text="New Game", command=start_new_game)

new_game_button.grid(column=0, row=1, sticky=(E, W), pady=(10, 0))

root.mainloop()
