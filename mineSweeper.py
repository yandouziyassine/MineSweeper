import tkinter as tk
import random
from tkinter import messagebox

class Minesweeper:
    def __init__(self, master, rows=10, columns=10, mines=10):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.buttons = []
        self.mine_positions = set()
        self.create_widgets()
        self.place_mines()

    def create_widgets(self):
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                button = tk.Button(self.master, width=2, command=lambda r=r, c=c: self.click(r, c))
                button.bind("<Button-3>", lambda e, r=r, c=c: self.right_click(r, c))
                button.grid(row=r, column=c)
                row.append(button)
            self.buttons.append(row)

    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.columns - 1)
            self.mine_positions.add((r, c))

    def click(self, r, c):
        if (r, c) in self.mine_positions:
            self.buttons[r][c].config(text="*", bg="red")
            messagebox.showinfo("Game Over", "You clicked on a mine!")
            self.master.destroy()
        else:
            self.reveal(r, c)

    def right_click(self, r, c):
        self.buttons[r][c].config(text="F")

    def reveal(self, r, c):
        if self.buttons[r][c]["text"] == "":
            mines_count = self.count_mines(r, c)
            self.buttons[r][c].config(text=str(mines_count), state="disabled")
            if mines_count == 0:
                for i in range(max(0, r-1), min(self.rows, r+2)):
                    for j in range(max(0, c-1), min(self.columns, c+2)):
                        if (i, j) != (r, c):
                            self.reveal(i, j)

    def count_mines(self, r, c):
        count = 0
        for i in range(max(0, r-1), min(self.rows, r+2)):
            for j in range(max(0, c-1), min(self.columns, c+2)):
                if (i, j) in self.mine_positions:
                    count += 1
        return count

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root)
    root.mainloop() 