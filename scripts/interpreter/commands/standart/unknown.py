from scripts.interpreter.commands.blocks.procedure import Procedure
from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.standart.creating import Creating
from scripts.interpreter.commands.variables.variable import Variable


class Unknown(Command):
    creating = Creating.none

    """
    Handles unknown commands
    """

    def __init__(self, interpreter):
        """
        Constructor

        :param interpreter: instance of interpreter
        """
        super().__init__(interpreter, '__UNKNOWN__')

    def set_creating(self, value):
        """
        Sets what will be created: a proc or a var
        :param value:
        """

        Unknown.creating = value

    @staticmethod
    def is_num(line):
        """
        Returns if line can be converted to an integer

        :param line: line to convert
        :return: if line can be converted to an integer
        :rtype: bool
        """
        try:
            int(line)
            return True
        except ValueError:
            return False

    def reverse_execute(self, command_name, previous_result=None):
        """
        Creates a procedure or a variable or returns int value or raises a error if none else worked

        :param command_name: unknown command name
        :param previous_result: returned value from previous command execution
        """
        if Unknown.is_num(command_name):
            number = int(command_name)
            self.assert_if(number <= 1000, f'Given number value [{number}] is more than 1000')
            self.assert_if(number >= 1, f'Given number value [{number}] is less than 1')
            return int(command_name)

        if Unknown.creating == Creating.variable:
            var = Variable(self.interpreter, command_name, previous_result)
            self.interpreter.add_command(var)

        elif Unknown.creating == Creating.proc:
            proc = Procedure(self.interpreter, command_name, self.line)
            self.interpreter.add_command(proc)

        else:
            self.assert_if(
                False,
                f'Unknown command [{command_name}], maybe you forgot to call SET / PROCEDURE'
            )

        Unknown.creating = Creating.none
