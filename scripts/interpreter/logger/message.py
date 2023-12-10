from enum import Enum
from datetime import datetime


class MessageType(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class Message:
    def __init__(self, test: str, type=MessageType.DEBUG):
        self.time = datetime.now()
        self.text = test
        self.type = type
