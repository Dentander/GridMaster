from scripts.interpreter.commands.command import Command


class Variable(Command):
    """
    Variable

    address: address in interpreter.variables to get value
    """

    def __init__(self, interpreter, name, value):
        """
        Creates variable in interpreter.variables

        :param interpreter: instance of interpreter
        :param name: variable name
        :param value: variable value
        """

        super().__init__(interpreter)
        self.name = name

        self.address = len(self.interpreter.variables)
        self.interpreter.variables.append(value)

    def reverse_execute(self, previous_result=None):
        """
        Getter and setter of variable

        :param previous_result: value of setter
        :return: self value
        """

        if previous_result is not None:
            self.interpreter.variables[self.address] = previous_result
        return self.interpreter.variables[self.address]
