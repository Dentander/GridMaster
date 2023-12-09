class Command:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.logger = interpreter.logger
        self.actor = interpreter.actor
        self.script = interpreter.script

        self.set_name()
        self.line = None

    def set_line(self, line):
        self.line = line
        return self

    def set_name(self):
        self.name = None

    def execute(self, previous_result=None):
        pass
