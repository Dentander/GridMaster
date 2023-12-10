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

    def execute(self, command_name, previous_result=None):
        if command_name.isdigit():
            return int(command_name)

        if Unknown.creating == Creating.variable:
            var = Variable(self.interpreter, command_name, previous_result)
            self.interpreter.add_command(var)

        if Unknown.creating == Creating.proc:
            proc = Procedure(self.interpreter, command_name, self.line)
            self.interpreter.add_command(proc)

        Unknown.creating = Creating.none
