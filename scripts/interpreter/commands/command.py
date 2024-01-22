class Command:
    """
    Abstract class of a command

    interpreter: instance of interpreter
    unknown: command that handles unknown command
    actor: instance of actor
    field: instance of field
    script: all script text
    name: command name to find command in script
    line: line in script on which this command was found
    """

    def __init__(self, interpreter, name=None):
        """
        Command constructor

        :param interpreter: instance of interpreter
        :param name: command name to find command in script
        """

        self.interpreter = interpreter
        if name != '__UNKNOWN__':
            self.unknown = interpreter.commands['__UNKNOWN__']
        self.actor = interpreter.actor
        self.field = interpreter.field
        self.script = interpreter.script
        self.name = name
        self.line = None

    def set_line(self, line):
        """
        Sets the line position in script and returns self

        :param line:
        :return: self
        """

        self.line = line
        return self

    def assert_if(self, condition, error_text):
        """
        If condition is False raises error with text

        :param condition: condition to check for errors
        :param error_text: text which will be shown if condition is False
        :rtype: bool
        """

        return self.interpreter.assert_if(condition, error_text)

    def direct_execute(self, previous_result=None):
        """
        Is called when command with it's name was found in line, direct_execute is called from left to right

        :param previous_result: returned value from previous command execution
        """

        pass

    def reverse_execute(self, previous_result=None):
        """
        Is called when command with it's name was found in line, reverse_execute is called from right to left after direct_execute

        :param previous_result: returned value from previous command execution
        """

        pass
