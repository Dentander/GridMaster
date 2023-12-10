from scripts.interpreter.commands.command import Command


class Right(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'RIGHT')

    def execute(self, previous_result=None):
        if previous_result is None:
            return 1, 0
        self.actor.move(previous_result, 0)
