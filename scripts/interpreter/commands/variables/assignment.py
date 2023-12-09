from scripts.interpreter.commands.command import Command


class Assignment(Command):
    def on_init(self):
        self.name = "="

    def execute(self, previous_result=None):
        return previous_result
