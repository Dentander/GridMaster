from scripts.interpreter.logger.message import MessageType


class Actor:
    def __init__(self, interpreter, position=(0, 0)):
        self.field = interpreter.field
        self.logger = interpreter.logger
        self.position_x, self.position_y = position

    def move(self, delta_x, delta_y):
        new_position_x, new_position_y = self.position_x + delta_x, self.position_y + delta_y

        if self.field.is_out(new_position_x, self.position_y):
            self.logger.log("Actor is out of field", MessageType.ERROR)
            return

        self.position_x, self.position_y = new_position_x, new_position_y

