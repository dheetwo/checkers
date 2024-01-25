from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("black")
        self.player2 = Player("red")

        self.test_two_piece_start()

        print(self.board.space_at_coordinates((3, 3)).piece.available_moves_list(self.board))
        print(self.board.space_at_coordinates((4, 4)).piece.available_moves_list(self.board))



    def test_two_piece_start(self):  # for testing purposes only
        self.player1.place_piece_on_board(self.board, (3, 3))
        self.player2.place_piece_on_board(self.board, (4, 4))
