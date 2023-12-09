from scripts.interpreter.commands.command import Command


class Repeat(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter)
        self.name = 'REPEAT'
        self.index = None

    def execute(self, previous_result=None):
        if self.index is None:
            self.index = previous_result
            self.interpreter.blocks_stack.append(self)

        if self.index <= 0:
            end = EndRepeat(self.interpreter).name
            new_line = self.interpreter.find_block_end(self.line, self.name, end)
            self.interpreter.goto(new_line)
            self.interpreter.blocks_stack.pop()
        self.index -= 1


class EndRepeat(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter)
        self.name = 'ENDREPEAT'

    def execute(self, previous_result=None):
        repeat_loop = self.interpreter.blocks_stack[-1]
        self.interpreter.goto(repeat_loop.line)
        repeat_loop.execute()
