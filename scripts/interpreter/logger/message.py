from enum import Enum
from datetime import datetime


class MessageType(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class Message:
    def __init__(self, test: str, line: int, type=MessageType.DEBUG):
        self.time = datetime.now()
        self.text = test
        self.line = line
        self.type = type

    def __str__(self):
        message_type = str(self.type).replace('MessageType.', '')
        message_time = str(self.time).split('.')[0]
        return f'| {message_type} | TIME: {message_time} | LINE: {self.line+1} | {self.text}'
