class Field:
    def __init__(self, size=(21, 21)):
        self.width, self.height = size

    def is_out(self, position: tuple):
        position_x, position_y = position
        return 0 <= position_x < self.width and 0 <= position_y < self.height

    def is_out(self, position_x: int, position_y: int):
        return 0 <= position_x < self.width and 0 <= position_y < self.height
