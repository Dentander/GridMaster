from scripts.interpreter.commands.command import Command


class Right(Command):
    def on_init(self):
        self.name = 'RIGHT'

    def execute(self, previous_result=None):
        self.actor.move(previous_result, 0)
