from scripts.interpreter.commands.command import Command
from scripts.interpreter.commands.standart.creating import Creating


class Procedure(Command):
    def __init__(self, interpreter, name, proc_line):
        super().__init__(interpreter, name)
        self.proc_line = proc_line

    def execute(self, previous_result=None):
        print("AXAXAXAX")
        self.interpreter.blocks_stack.append(self)
        self.interpreter.goto(self.proc_line)


class CreateProc(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'PROCEDURE')

    def pre_execute(self):
        self.unknown.set_creating(Creating.proc)

    def execute(self, previous_result=None):
        end = EndProc(self.interpreter).name
        new_line = self.interpreter.find_block_end(self.line, self.name, end)
        self.interpreter.goto(new_line)


class EndProc(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'ENDPROC')

    def execute(self, previous_result=None):
        proc = self.interpreter.blocks_stack.pop()
        self.interpreter.goto(proc.line)


class Call(Command):
    def __init__(self, interpreter):
        super().__init__(interpreter, 'CALL')

