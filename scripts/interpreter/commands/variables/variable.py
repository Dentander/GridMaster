from scripts.interpreter.commands.command import Command


class Variable(Command):
    def __init__(self, interpreter, name, value):
        super().__init__(interpreter)
        self.name = name

        self.interpreter.variables.append(value)
        self.address = len(self.interpreter.variables)
        self.interpreter.variables.append(value)

    def reverse_execute(self, previous_result=None):
        if previous_result is not None:
            self.interpreter.variables[self.address] = previous_result
        return self.interpreter.variables[self.address]
