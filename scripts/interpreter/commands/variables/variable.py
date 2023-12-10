from scripts.interpreter.commands.command import Command


class Variable(Command):
    count = 0

    def __init__(self, interpreter, name, value):
        super().__init__(interpreter, name)

        self.interpreter.variables.append(value)
        self.address = Variable.count
        Variable.count += 1

    def execute(self, previous_result=None):
        if previous_result is not None:
            self.interpreter.variables[self.address] = previous_result
        return self.interpreter.variables[self.address]
