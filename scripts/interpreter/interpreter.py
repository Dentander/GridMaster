from scripts.interpreter.actor import Actor
from scripts.interpreter.commands.repeat import Repeat, EndRepeat
from scripts.interpreter.field import Field
from scripts.interpreter.logger.logger import *
from scripts.interpreter.commands.print import Say
from copy import copy


class Interpreter:
    def __init__(self):
        self.logger = Logger()
        self.field = Field()
        self.actor = Actor(self)

        self.script = []
        self.commands = {}
        self.blocks_stack = []
        self.variables = []

        self.current_line = 0

        self.add_all_commands()

    def read_file(self, file_name: str):
        with open(file_name) as file:
            self.script = file.readlines()

    def add_all_commands(self):
        self.add_command(Say(self))
        self.add_command(Repeat(self))
        self.add_command(EndRepeat(self))

    def add_command(self, command):
        self.commands[command.name] = command

    def execute_current_line(self):
        commands = self.script[self.current_line].split()
        self.execute_commands(commands)
        self.current_line += 1

    def execute_commands(self, commands: list, current_command=0):
        command_name = commands[current_command]

        if command_name[0] in "0123456789":
            return int(command_name)

        command = copy(self.commands[command_name].set_line(self.current_line))

        if current_command == len(commands) - 1:
            return command.execute(None)

        return command.execute(self.execute_commands(commands, current_command+1))

    def goto(self, line: int):
        self.current_line = line

    def run(self):
        while self.current_line < len(self.script):
            self.execute_current_line()
