from scripts.interpreter.commands.command import Command


class Assignment(Command):
    """
    Assigns a value to a variable
    """

    def __init__(self, interpreter):
        """
        Constructor

        :param interpreter: instance of interpreter
        """

        super().__init__(interpreter, "=")

    def reverse_execute(self, previous_result=None):
        """
        Just passes previous_result

        :param previous_result:
        """

        return previous_result
