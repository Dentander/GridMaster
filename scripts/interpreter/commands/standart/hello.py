from scripts.interpreter.commands.command import Command


class Hello(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'HELLO')

    def execute(self, previous_result=None):
        print('Hello', self.line)
