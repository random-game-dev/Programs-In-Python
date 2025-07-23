import tkinter as tk
import random

GRID_SIZE = 10
NUM_MINES = 10

class Cell:
    def __init__(self, button, x, y):
        self.button = button
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_revealed = False
        self.neighbor_mines = 0

def place_mines(cells):
    mines = random.sample(cells, NUM_MINES)
    for cell in mines:
        cell.is_mine = True

def calculate_neighbors(cells):
    for cell in cells:
        x, y = cell.x, cell.y
        neighbors = [c for c in cells if abs(c.x - x) <= 1 and abs(c.y - y) <= 1 and c != cell]
        cell.neighbor_mines = sum(n.is_mine for n in neighbors)

def reveal(cell):
    if cell.is_revealed or cell.button["text"] == "🚩":
        return
    cell.is_revealed = True
    if cell.is_mine:
        cell.button.config(text="💣", bg="red")
    else:
        cell.button.config(text=str(cell.neighbor_mines or ""), bg="lightgray")
        if cell.neighbor_mines == 0:
            x, y = cell.x, cell.y
            for neighbor in cells:
                if abs(neighbor.x - x) <= 1 and abs(neighbor.y - y) <= 1:
                    reveal(neighbor)

def toggle_flag(event, cell):
    if cell.is_revealed:
        return
    current = cell.button["text"]
    if current == "🚩":
        cell.button.config(text="")
    else:
        cell.button.config(text="🚩")

# GUI setup
window = tk.Tk()
window.title("💥 Python Minesweeper")
frame = tk.Frame(window)
frame.pack()

cells = []

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        btn = tk.Button(frame, width=3, height=1, font=("Consolas", 14), relief="raised")
        btn.grid(row=x, column=y)
        cell = Cell(btn, x, y)
        btn.config(command=lambda c=cell: reveal(c))
        btn.bind("<Button-3>", lambda e, c=cell: toggle_flag(e, c))
        cells.append(cell)

place_mines(cells)
calculate_neighbors(cells)

window.mainloop()