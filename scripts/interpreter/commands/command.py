class Command:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.logger = interpreter.logger
        self.actor = interpreter.actor
        self.script = interpreter.script
        self.name = None
        self.line = None
        self.on_init()

    def set_line(self, line):
        self.line = line
        return self

    def on_init(self):
        pass

    def execute(self, previous_result=None):
        pass
