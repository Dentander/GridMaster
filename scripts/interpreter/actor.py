class Actor:
    def __init__(self, interpreter, position=(0, 0)):
        self.interpreter = interpreter
        self.field = interpreter.field
        self.logger = interpreter.logger
        self.position_x, self.position_y = position

    def move(self, delta_x, delta_y):
        new_position_x, new_position_y = self.position_x + delta_x, self.position_y + delta_y

        if self.field.is_out(new_position_x, self.position_y):
            self.interpreter.assert_if(False, "Actor is out of field")
            return

        self.position_x, self.position_y = new_position_x, new_position_y
