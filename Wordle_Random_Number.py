#Tkinter Lessons
import tkinter as tk
from tkinter import font as tkfont

BG = "#FF0000"
TEXT = "#008080"
SUBTLE = "#000000"


app = tk.Tk()
app.title("Wordle")
app.configure(bg=BG)
app.resizable(False, False)
app.geometry("400x600")

 
title_font  = tkfont.Font(family="Fredoka One", size=22, weight="bold")
legend_font = tkfont.Font(family="Fredoka One", size=11)
 
# ── Header 
header = tk.Frame(app, bg=BG)
header.pack(pady=(18, 4))
tk.Label(header, text="WORDLE", font=title_font,
         bg=BG, fg=TEXT).pack()
 
# ── Separator line ──────────────────────────────────
sep = tk.Frame(app, bg="#00FF00", height=1)
sep.pack(fill="x", padx=20, pady=(4, 0))
 
# ── Legend ──────────────────────────────────────────
legend = tk.Frame(app, bg=BG)
legend.pack(pady=(10, 0))
 
legend_items = [
    ("🟩", "Correct position"),
    ("🟨", "Wrong position"),
    ("🟧", "Wrong position — duplicate still hiding"),
    ("⬛", "Not in word"),
]
 
for emoji, desc in legend_items:
    row = tk.Frame(legend, bg=BG)
    row.pack(anchor="w", padx=24)
    tk.Label(row, text=f"{emoji}  {desc}",
             font=legend_font, bg=BG, fg=SUBTLE).pack(side="left")

# Grid Section

TILE_EMPTY  = "#008080"
TILE_BORDER = "#00FF00"
TILE_SIZE   = 58
GAP         = 5
 
tile_font = tkfont.Font(family="Fredoka One", size=26, weight="bold")
 
grid_frame = tk.Frame(app, bg=BG)
grid_frame.pack(pady=16)
 
tiles  = []   # tiles[row][col]  → Frame
labels = []   # labels[row][col] → Label
 
for r in range(6):
    row_tiles  = []
    row_labels = []
    for c in range(5):
        frame = tk.Frame(
            grid_frame,
            width=TILE_SIZE, height=TILE_SIZE,
            bg=TILE_EMPTY,
            highlightbackground=TILE_BORDER,
            highlightthickness=2,
        )
        frame.grid(row=r, column=c,
                   padx=GAP // 2, pady=GAP // 2)
        frame.grid_propagate(False)  # lock to TILE_SIZE
 
        lbl = tk.Label(
            frame, text="",
            font=tile_font,
            bg=TILE_EMPTY, fg="#0000FF",
            anchor="center",
        )

    
    
app.mainloop() 
