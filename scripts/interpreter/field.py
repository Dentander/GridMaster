class Field:
    """
    Field along which the actor moves

    width: field width
    height: field height
    """

    def __init__(self, size=(21, 21)):
        """
        Field constructor

        :param size: field size
        """

        self.width, self.height = size

    def is_out(self, position: tuple):
        """
        Returns if object is out of field

        :param position: current object position
        :rtype: bool
        """

        position_x, position_y = position
        return not (0 <= position_x < self.width and 0 <= position_y < self.height)

    def is_out(self, position_x: int, position_y: int):
        """
        Returns if object is out of field

        :param position_x: current object position x
        :param position_y: current object position y
        :rtype: bool
        """

        return not (0 <= position_x < self.width and 0 <= position_y < self.height)

    def draw(self, actor):
        """
        Draws field in console

        :param actor: main actor to get his current position
        :return: None
        """

        print('#' * (self.width + 2))
        for y in range(self.height)[::-1]:
            line = '#' + '-' * self.width + '#'
            if actor.position_y == y:
                line = line[:actor.position_x+1] + '*' + line[actor.position_x+2:]
            print(line)
        print('#' * (self.width + 2))
        print()
