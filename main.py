import tkinter as tk
from checkers import Game
from GameGUI import GameGUI

if __name__ == "__main__":
    game = Game()
    game_gui = GameGUI(game)
    game_gui.draw_board()