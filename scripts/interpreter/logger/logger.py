from scripts.interpreter.logger.message import *


class Logger:
    def __init__(self):
        self.messages = []

    def log(self, message: Message):
        self.messages.append(message)
        print(message.text)

    def log(self, message_test: str, message_type=MessageType.DEBUG):
        self.messages.append(Message(message_test, message_type))
        print(message_test)

    def clear(self):
        self.messages.clear()
