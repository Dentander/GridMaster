from scripts.interpreter.commands.command import Command


class Down(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'DOWN')

    def reverse_execute(self, previous_result=None):
        if previous_result is None:
            return 0, -1
        self.actor.move(0, -previous_result)
