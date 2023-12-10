from scripts.interpreter.commands.command import Command


class Up(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'UP')

    def execute(self, previous_result=None):
        if previous_result is None:
            return 0, 1
        self.actor.move(0, previous_result)
