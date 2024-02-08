class Actor:
    """
    Object that moves across the field

    interpreter: instance of interpreter
    field: instance of field
    position_x: position along X axis
    position_y: position along Y axis
    """
    def __init__(self, interpreter, position=(0, 0)):
        """
        Actor constructor

        :param interpreter: instance of interpreter
        :param position: actor's initial position
        """

        self.interpreter = interpreter
        self.field = interpreter.field
        self.position_x, self.position_y = position

    def move(self, delta_x, delta_y):
        """
        Moves actor and checks if actor is out of field

        :param delta_x: the distance the actor moves along the X axis
        :param delta_y: the distance the actor moves along the Y axis
        :return:
        """

        new_position_x, new_position_y = self.position_x + delta_x, self.position_y + delta_y

        if self.field.is_out(new_position_x, self.position_y):
            self.interpreter.assert_if(False, "ACTOR IS OUT OF FIELD")
            return

        self.position_x, self.position_y = new_position_x, new_position_y

    def getX(self):
        return self.position_x
    
    def getY(self):
        return self.position_y
    