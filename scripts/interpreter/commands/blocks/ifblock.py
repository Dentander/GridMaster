from scripts.interpreter.commands.command import Command
from scripts.interpreter.logger.message import MessageType


class IfBlock(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'IFBLOCK')

    def reverse_execute(self, previous_result=None):
        if self.assert_if(
                isinstance(previous_result, tuple),
                f'INVALID INPUT FOR IFBLOCK [{previous_result}]'
        ):
            return

        delta_x, delta_y = previous_result
        if self.field.is_out(self.actor.position_x + delta_x, self.actor.position_y + delta_y):
            self.interpreter.blocks_stack.append(self)
            return

        end = EndIf(self.interpreter).name
        new_line = self.interpreter.find_block_end(self.line, self.name, end)
        self.interpreter.goto(new_line)


class EndIf(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'ENDIF')

    def reverse_execute(self, previous_result=None):
        self.assert_if(len(self.interpreter.blocks_stack) > 0, 'TO MANY END COMMANDS')
        block = self.interpreter.blocks_stack[-1]
        self.assert_if(
            block.name == IfBlock(self.interpreter).name,
            f'YOU ARE TRYING TO END [{block.name}] WITH [{self.name}]'
        )
        self.interpreter.blocks_stack.pop()
