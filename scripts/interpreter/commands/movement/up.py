from scripts.interpreter.commands.command import Command


class Up(Command):
    def on_init(self):
        self.name = 'UP'

    def execute(self, previous_result=None):
        self.actor.move(0, previous_result)
