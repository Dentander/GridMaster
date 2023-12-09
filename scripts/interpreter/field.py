class Field:
    def __init__(self, size=(21, 21)):
        self.width, self.height = size

    def is_out(self, position: tuple):
        position_x, position_y = position
        return not (0 <= position_x < self.width and 0 <= position_y < self.height)

    def is_out(self, position_x: int, position_y: int):
        return not (0 <= position_x < self.width and 0 <= position_y < self.height)

    def draw(self, actor):
        print('#' * (self.width + 2))
        for y in range(self.height)[::-1]:
            line = '#' + '-' * self.width + '#'
            if actor.position_y == y:
                line = line[:actor.position_x+1] + '*' + line[actor.position_x+2:]
            print(line)
        print('#' * (self.width + 2))
        print()



