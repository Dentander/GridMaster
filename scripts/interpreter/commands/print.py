from scripts.interpreter.commands.command import Command


class Say(Command):
    def set_name(self):
        self.name = 'HELLO'

    def execute(self, previous_result=None):
        print("Hello")
