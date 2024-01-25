class Board:
    def __init__(self):
        GRID_WIDTH = 8
        GRID_HEIGHT = 8

        # grid_mapping: list of lists  containing (coordinates, Space)
        # coordinates: tuple (x, y); Space: parameters, brown or white
        self.grid_mapping = []

        # Populate the grid_mapping with (coordinate, Space) tuple-pairs
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if (x + y) % 2 == 0:  # green squares
                    self.grid_mapping.append([(x, y), Space("green")])
                else:
                    self.grid_mapping.append([(x, y), Space("white")])


    def space_at_coordinates(self, coordinates):
        try:
            for coord, space in self.grid_mapping:
                if coord == coordinates:
                    return space
            # Raise an exception if coordinates are not found in the grid_mapping
            raise ValueError(f"No space found at coordinates {coordinates}")
        except ValueError as e:
            print(e)
            return None

class Space:
    def __init__(self, color):
        self.color = color
        self.piece = None