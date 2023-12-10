from scripts.interpreter.commands.command import Command


class Set(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'SET')

    def execute(self, previous_result=None):
        pass
