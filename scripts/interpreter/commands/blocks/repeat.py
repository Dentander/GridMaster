from scripts.interpreter.commands.command import Command


class Repeat(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'REPEAT')
        self.index = None

    def reverse_execute(self, previous_result=None):
        if self.assert_if(
                isinstance(previous_result, int) or (previous_result is None and self.index is not None),
                f'NOT VALID INPUT FOR REPEAT [{previous_result}]'
        ):
            return

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
        super().__init__(interpreter, 'ENDREPEAT')

    def reverse_execute(self, previous_result=None):
        self.assert_if(len(self.interpreter.blocks_stack) > 0, 'TO MANY END COMMANDS')
        block = self.interpreter.blocks_stack[-1]
        self.assert_if(
            block.name == Repeat(self.interpreter).name,
            f'YOU ARE TRYING TO CLOSE [{block.name}] WITH [{self.name}]'
        )
        self.interpreter.goto(block.line)
        block.reverse_execute()
