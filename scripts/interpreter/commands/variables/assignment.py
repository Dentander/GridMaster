from scripts.interpreter.commands.command import Command


class Assignment(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, "=")

    def reverse_execute(self, previous_result=None):
        return previous_result
