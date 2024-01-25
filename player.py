class Player:
    def __init__(self, color):
        self.color = color
        self.direction = {"black": 1, "red": -1}.get(self.color)

    def place_piece_on_board(self, board, coordinates):
        board.space_at_coordinates(coordinates).piece = Piece(self.color, coordinates)

    def move_piece_on_board(self, board, coordinates):
        pass

class Piece:
    def __init__(self, color, coordinates, is_king=False):
        self.color = color
        self.coordinates = coordinates
        self.is_king = is_king
        self.direction = {"black": 1, "red": -1}.get(self.color)

    def available_moves_list(self, board):
        x = self.coordinates[0]
        y = self.coordinates[1]

        # search diagonals on board for empty Spaces
        search_list = [(x - 1, y + self.direction), (x + 1, y + self.direction)]
        if self.is_king:
            search_list.extend([(x - 1, y - self.direction), (x - 1, y - self.direction)])
        search_list = [(x, y) for x, y in search_list if all(coord in range(0, 8) for coord in (x, y))]
        search_list = [coordinates for coordinates in search_list if
                       type(board.space_at_coordinates(coordinates).piece) is not Piece]
        return search_list

    def available_captures_list(self, board):
        pass