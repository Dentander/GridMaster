from scripts.interpreter.logger.message import *


class Logger:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.messages = []

    def debug(self, message_test: str, line=None):
        if line is None:
            line = self.interpreter.line
        self.messages.append(Message(message_test, line, MessageType.DEBUG))
        print(self.messages[-1])

    def info(self, message_test: str, line=None):
        if line is None:
            line = self.interpreter.line
        self.messages.append(Message(message_test, line, MessageType.INFO))
        print(self.messages[-1])

    def warning(self, message_test: str, line=None):
        if line is None:
            line = self.interpreter.line
        self.messages.append(Message(message_test, line, MessageType.WARNING))
        print(self.messages[-1])

    def error(self, message_test: str, line=None):
        if line is None:
            line = self.interpreter.line
        self.messages.append(Message(message_test, line, MessageType.ERROR))
        print(self.messages[-1])
        return self.messages[-1].__str__()

    def clear(self):
        self.messages.clear()
