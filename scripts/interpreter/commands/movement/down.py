from scripts.interpreter.commands.command import Command


class Down(Command):
    """
    Moves actor down or returns direction
    """

    def __init__(self, interpreter):
        """
        Constructor

        :param interpreter: instance of interpreter
        """

        super().__init__(interpreter, 'DOWN')

    def reverse_execute(self, previous_result=None):
        """
        Moves actor down or returns direction

        :param previous_result: blocks down count
        """

        if previous_result is None:
            return 0, -1
        self.actor.move(0, -previous_result)
