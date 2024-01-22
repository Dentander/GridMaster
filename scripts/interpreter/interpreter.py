from scripts.interpreter.commands.blocks.ifblock import IfBlock, EndIf
from scripts.interpreter.commands.blocks.procedure import CreateProc, EndProc, Call
from scripts.interpreter.commands.movement.down import Down
from scripts.interpreter.commands.movement.left import Left
from scripts.interpreter.commands.movement.right import Right
from scripts.interpreter.commands.movement.up import Up
from scripts.interpreter.commands.standart.creating import Creating
from scripts.interpreter.commands.variables.assignment import Assignment
from scripts.interpreter.commands.blocks.repeat import Repeat, EndRepeat
from scripts.interpreter.commands.variables.set import Set
from scripts.interpreter.commands.standart.unknown import Unknown

from scripts.interpreter.logger.logger import Logger
from scripts.interpreter.field import Field
from scripts.interpreter.actor import Actor

from copy import copy


class Interpreter:
    def __init__(self):
        """
        Constructor
        """

        self.logger = Logger(self)
        self.field = Field()
        self.actor = Actor(self)

        self.script = []
        self.commands = {}
        self.blocks_stack = []
        self.variables = []
        self.line = 0
        self.got_error = False

        self.add_all_commands()

    def reset(self):
        """
        Resets interpreter
        """

        self.logger = Logger(self)
        self.field = Field()
        self.actor = Actor(self)

        self.script = []
        self.commands = {}
        self.blocks_stack = []
        self.variables = []
        self.line = 0
        self.got_error = False
        self.add_all_commands()

    def add_all_commands(self):
        """
        Adds all command to self.commands dict
        """

        self.add_command(Unknown(self))

        self.add_command(Repeat(self))
        self.add_command(EndRepeat(self))
        self.add_command(Assignment(self))
        self.add_command(Set(self))
        self.add_command(Right(self))
        self.add_command(Left(self))
        self.add_command(Up(self))
        self.add_command(Down(self))
        self.add_command(IfBlock(self))
        self.add_command(EndIf(self))
        self.add_command(CreateProc(self))
        self.add_command(EndProc(self))
        self.add_command(Call(self))

    def add_command(self, command):
        """
        Adds a command to self.commands dict

        :param command: command to add
        """

        self.commands[command.name] = command

    def read_file(self, file_name: str):
        """
        Reads script from file

        :param file_name: file_name to read
        """

        with open(file_name) as file:
            self.script = file.readlines()

    def execute_current_line(self):
        """
        Executes only current line
        """
        line = self.line

        commands = self.script[self.line].split()
        self.execute_commands(commands)

        self.assert_if(
            Unknown.creating != Creating.proc,
            'YOU ARE TRYING TO CREATE A PROC THAT ALREADY EXISTS',
            line
        )

        if not self.got_error:
            self.line += 1
        Unknown.creating = Creating.none

    def execute_commands(self, commands: list, current_command=0):
        """
        Executes a list of commands

        :param commands: commands list
        :param current_command: current command index in commands list
        """

        self.assert_if(len(self.blocks_stack) <= 3, 'DEPTH LEVEL IS GREATER THAN 3')

        if current_command == len(commands) or self.got_error:
            return None

        command_name = commands[current_command]
        if command_name not in self.commands.keys():
            command = copy(self.commands['__UNKNOWN__']).set_line(self.line)
            command.direct_execute(command_name)
            return command.reverse_execute(command_name, self.execute_commands(commands, current_command + 1))

        command = copy(self.commands[command_name]).set_line(self.line)
        command.direct_execute()

        try:
            return command.reverse_execute(self.execute_commands(commands, current_command + 1))
        except Exception as error:
            self.assert_if(False, f'UNKNOWN ERROR: {error}')

    def goto(self, line: int):
        """
        Goes to line

        :param line: line to go
        """

        if self.got_error:
            return

        self.line = line

    def assert_if(self, condition: bool, error_text: str, line=None):
        """
        If condition is False raises error with text

        :param condition: condition to check for errors
        :param error_text: text which will be shown if condition is False
        :param line: line on which the error occurred
        :rtype: bool
        """

        if condition:
            return False

        self.logger.error(error_text, line)
        self.got_error = True
        return True

    def find_block_end(self, line: int, block_begin: str, block_end: str):
        """
        Finds block_end line position to end block_begin

        :param line: current line
        :param block_begin: block begin name
        :param block_end: block end name
        :return: block_end line position
        """

        local_depth = 1
        while local_depth > 0 and line + 1 < len(self.script):
            line += 1
            commands = self.script[line].split()
            if len(commands) == 0:
                continue

            command = commands[0]
            local_depth += command == block_begin
            local_depth -= command == block_end

        self.assert_if(
            line < len(self.script) and block_end in self.script[line],
            f'COULD NOT FIND [{block_end}] TO END [{block_begin}]'
        )
        return line

    def run(self):
        """
        Executes the script completely
        """

        while self.finished() is False:
            print(self.line)
            self.execute_current_line()
            self.field.draw(self.actor)
            if self.got_error:
                break

    def finished(self):
        return self.line >= len(self.script) or self.got_error
