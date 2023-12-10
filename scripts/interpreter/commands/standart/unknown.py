from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.variables.variable import Variable


class Unknown(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, '__UNKNOWN__')

    def execute(self, command_name, previous_result=None):
        if command_name.isdigit():
            return int(command_name)

        if previous_result is not None:
            var = Variable(self.interpreter, command_name, previous_result)
            self.interpreter.add_command(var)
