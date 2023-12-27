from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.standart.unknown import Unknown, Creating


class Set(Command):
    """
    Command that tells that a variable is created
    """

    def __init__(self, interpreter):
        """
        Constructor

        :param interpreter: instance of interpreter
        """

        super().__init__(interpreter, 'SET')

    def direct_execute(self, previous_result=None):
        """
        Prepares unknown command handler that a variable is created

        :param previous_result:
        """

        self.unknown.set_creating(Creating.variable)
        return Creating.variable
