from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.standart.unknown import Unknown, Creating


class Set(Command):

    def __init__(self, interpreter):
        super().__init__(interpreter, 'SET')

    def direct_execute(self, previous_result=None):
        self.unknown.set_creating(Creating.variable)
        return Creating.variable
