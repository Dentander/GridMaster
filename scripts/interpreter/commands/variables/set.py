from scripts.interpreter.commands.command import Command


class Set(Command):
    def on_init(self):
        self.name = "SET"

    def execute(self, previous_result=None):
        pass
