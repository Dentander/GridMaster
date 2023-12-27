from scripts.interpreter.commands.command import Command


class Left(Command):
    """
    Moves actor left or returns direction
    """

    def __init__(self, interpreter):
        """
        Constructor

        :param interpreter: instance of interpreter
        """

        super().__init__(interpreter, 'LEFT')

    def reverse_execute(self, previous_result=None):
        """
        Moves actor left or returns direction

        :param previous_result: blocks left count
        """

        if previous_result is None:
            return -1, 0
        self.actor.move(-previous_result, 0)
