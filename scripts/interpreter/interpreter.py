from scripts.interpreter.actor import Actor
from scripts.interpreter.commands.variables.assignment import Assignment
from scripts.interpreter.commands.blocks.repeat import Repeat, EndRepeat
from scripts.interpreter.commands.variables.set import Set
from scripts.interpreter.commands.standart.unknown import Unknown
from scripts.interpreter.field import Field
from scripts.interpreter.logger.logger import *
from scripts.interpreter.commands.standart.hello import Hello
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
        self.line = 0

        self.add_all_commands()

    def add_all_commands(self):
        self.add_command(Hello(self))
        self.add_command(Repeat(self))
        self.add_command(EndRepeat(self))
        self.add_command(Unknown(self))
        self.add_command(Assignment(self))
        self.add_command(Set(self))

    def read_file(self, file_name: str):
        with open(file_name) as file:
            self.script = file.readlines()

    def add_command(self, command):
        self.commands[command.name] = command

    def execute_current_line(self):
        commands = self.script[self.line].split()
        self.execute_commands(commands)
        self.line += 1

    def execute_commands(self, commands: list, current_command=0):
        if current_command == len(commands):
            return None
        command_name = commands[current_command]

        if command_name not in self.commands.keys():
            command = copy(self.commands["__UNKNOWN__"].set_line(self.line))
            return command.execute(command_name, self.execute_commands(commands, current_command+1))

        command = copy(self.commands[command_name].set_line(self.line))
        return command.execute(self.execute_commands(commands, current_command+1))

    def goto(self, line: int):
        self.line = line

    def find_block_end(self, line, block_begin, block_end):
        local_depth = 1
        while local_depth > 0:
            line += 1
            commands = self.script[line].split()
            if len(commands) == 0:
                continue

            command = commands[0]
            local_depth += command == block_begin
            local_depth -= command == block_end
        return line

    def run(self):
        while self.line < len(self.script):
            self.execute_current_line()
