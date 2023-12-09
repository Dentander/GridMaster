from scripts.interpreter.commands.command import Command


class Hello(Command):
    def on_init(self):
        self.name = "HELLO"

    def execute(self, previous_result=None):
        print('Hello', self.line)
