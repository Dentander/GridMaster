from enum import Enum
from datetime import datetime


class MessageType(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class Message:
    def __init__(self, message_test: str, message_type=MessageType.DEBUG):
        self.time = datetime.now()
        self.message_test = message_test
        self.message_type = message_type
