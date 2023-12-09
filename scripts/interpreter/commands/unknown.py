from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.variable import Variable


class Unknown(Command):
    def on_init(self):
        self.name = '__UNKNOWN__'

    def execute(self, command_name, previous_result=None):
        if command_name.isdigit():
            return int(command_name)

        if previous_result is not None and command_name not in self.interpreter.commands.keys():
            var = Variable(self.interpreter, command_name, previous_result)
            self.interpreter.add_command(var)

