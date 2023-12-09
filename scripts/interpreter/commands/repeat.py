from scripts.interpreter.commands.command import Command


class Repeat(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter)
        self.name = "REPEAT"
        self.index = None

    def execute(self, previous_result=None):
        if self.index is None:
            self.index = previous_result
            self.interpreter.blocks_stack.append(self)
        self.index -= 1


class EndRepeat(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter)
        self.name = "ENDREPEAT"

    def execute(self, previous_result=None):
        repeat_loop = self.interpreter.blocks_stack[-1]
        if repeat_loop.index > 0:
            repeat_loop.execute()
            self.interpreter.goto(repeat_loop.line)
        else:
            self.interpreter.blocks_stack.pop()
