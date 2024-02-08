from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.standart.creating import Creating


class Procedure(Command):
    def __init__(self, interpreter, name, proc_line):
        super().__init__(interpreter, name)
        self.proc_line = proc_line

    def reverse_execute(self, previous_result=None):
        self.interpreter.blocks_stack.append(self)
        self.interpreter.goto(self.proc_line)


class CreateProc(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'PROCEDURE')

    def direct_execute(self, previous_result=None):
        self.unknown.set_creating(Creating.proc)
        return Creating.proc

    def reverse_execute(self, previous_result=None):
        end = EndProc(self.interpreter).name
        new_line = self.interpreter.find_block_end(self.line, self.name, end)
        self.interpreter.goto(new_line)


class EndProc(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'ENDPROC')

    def reverse_execute(self, previous_result=None):
        if self.assert_if(len(self.interpreter.blocks_stack) > 0, 'TO MANY END COMMANDS'):
            return

        block = self.interpreter.blocks_stack[-1]

        if self.assert_if(
            block.name not in ['IFBLOCK', 'REPEAT'],
            f'YOU ARE TRYING TO END [{block.name}] WITH [{self.name}]'
        ):
            return

        block = self.interpreter.blocks_stack.pop()
        self.interpreter.goto(block.line)


class Call(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'CALL')
