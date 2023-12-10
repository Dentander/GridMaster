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

    def pre_execute(self):
        pass

    def execute(self, previous_result=None):
        pass
