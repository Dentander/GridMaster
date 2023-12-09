from scripts.interpreter.commands.command import Command


class Down(Command):
    def on_init(self):
        self.name = 'DOWN'

    def execute(self, previous_result=None):
        self.actor.move(0, -previous_result)
