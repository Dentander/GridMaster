from scripts.interpreter.commands.command import Command


class Left(Command):
    def on_init(self):
        self.name = 'LEFT'

    def execute(self, previous_result=None):
        self.actor.move(-previous_result, 0)
