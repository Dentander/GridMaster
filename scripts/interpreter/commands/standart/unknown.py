from scripts.interpreter.commands.blocks.procedure import Procedure
from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.standart.creating import Creating
from scripts.interpreter.commands.variables.variable import Variable


class Unknown(Command):
    creating = Creating.none

    def __init__(self, interpreter):
        super().__init__(interpreter, '__UNKNOWN__')

    def set_creating(self, value):
        Unknown.creating = value

    @staticmethod
    def is_num(line):
        try:
            int(line)
            return True
        except ValueError:
            return False

    def reverse_execute(self, command_name, previous_result=None):
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
