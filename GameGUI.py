import tkinter as tk

class GameGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.canvas_size = 400
        self.square_size = self.canvas_size // 8
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()

    def draw_board(self):
        for entry in self.game.board.grid_mapping:
            position, space = entry[0], entry[1]
            row, col = position[0], position[1]

            x1, y1 = col * self.square_size, (7 - row) * self.square_size
            x2, y2 = x1 + self.square_size, y1 + self.square_size

            space_color = space.color

            # Draw space
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=space_color)

            # Draw piece if it exists
            if space.piece is not None:
                piece_color = space.piece.color
                self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=piece_color)

        self.root.mainloop()
