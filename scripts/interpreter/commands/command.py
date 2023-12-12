class Command:
    def __init__(self, interpreter, name=None):
        self.interpreter = interpreter
        if name != '__UNKNOWN__':
            self.unknown = interpreter.commands['__UNKNOWN__']
        self.logger = interpreter.logger
        self.actor = interpreter.actor
        self.field = interpreter.field
        self.script = interpreter.script
        self.name = name
        self.line = None

    def set_line(self, line):
        self.line = line
        return self

    def assert_if(self, condition, error_text):
        if condition:
            return

        self.logger.error(error_text)
        self.interpreter.got_error = True

    def direct_execute(self, previous_result=None):
        pass

    def reverse_execute(self, previous_result=None):
        pass
